from django.db import models
from django.db.models import Prefetch

from Core.models import Publishing, SlugAndPublishingContain
from .validators import validate_brilliant


class Category(SlugAndPublishingContain):
    name = models.CharField('Название', max_length=150,
                            help_text='max 150 символов')
    weight = models.PositiveSmallIntegerField('Вес', default=100,
                                              help_text='max 32767 ,min 1')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.slug)


class Tag(SlugAndPublishingContain):
    name = models.CharField('Название', max_length=150,
                            help_text='max 150 символов')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return str(self.name)


class ItemManager(models.Manager):
    def item_and_tags_is_published(self):
        return Item.objects.all().filter(is_published=True).prefetch_related(
            Prefetch('tags',
                     queryset=Tag.objects.filter(is_published=True)))

    def item_category_tags_is_published(self):
        return Item.objects.select_related('category').filter(
            category__is_published=True).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.filter(is_published=True)))


class Item(Publishing):
    name = models.CharField('Название', max_length=150,
                            help_text='max 150 символов')
    text = models.TextField('Описание', default='empty',
                            help_text='min 2 слова, должно '
                                      'содержать превосходно или роскошно',
                            validators=[validate_brilliant])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='items',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]

    objects = ItemManager()
