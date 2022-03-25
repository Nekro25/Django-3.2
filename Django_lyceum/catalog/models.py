from django.db import models
from django.core import validators

from Core.models import Publishing, SlugAndPublishingContain
from .validators import validate_brilliant


class Category(SlugAndPublishingContain):
    weight = models.IntegerField('Вес', default=100, help_text='max 32767 ,min 1',
                                 validators=[validators.MaxValueValidator(32767),
                                             validators.MinValueValidator(1)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(SlugAndPublishingContain):
    is_published = models.BooleanField('Опубликованно', default=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Item(Publishing):
    name = models.CharField('Название', max_length=150, help_text='max 150 символов')
    text = models.TextField('Описание', default='empty',
                            help_text='min 2 слова, должно содержать превосходно или роскошно',
                            validators=[validate_brilliant])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name[:15]

