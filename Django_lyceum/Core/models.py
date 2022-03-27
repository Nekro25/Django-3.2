from django.core import validators
from django.db import models


class Publishing(models.Model):
    is_published = models.BooleanField('Опубликованно', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.is_published)


class SlugAndPublishingContain(Publishing):
    slug = models.CharField('Слаг', max_length=200,
                            help_text='max 200 символов',
                            validators=[validators.validate_slug], unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug[:15]
