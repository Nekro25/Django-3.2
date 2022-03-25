from django.db import models
from django.core import validators


class Publishing(models.Model):
    is_published = models.BooleanField('Опубликованно', default=True)

    class Meta:
        abstract = True


class SlugAndPublishingContain(Publishing):
    slug = models.CharField('Слаг', max_length=200, help_text='max 200 символов',
                            validators=[validators.validate_slug])

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug[:15]
