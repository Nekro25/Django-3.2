from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Item

User = get_user_model()


class Rating(models.Model):
    RATING_CHOICES = [
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь')
    ]
    star = models.IntegerField('Оценка', default=0, choices=RATING_CHOICES,
                               null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name='Товар')

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [models.UniqueConstraint(fields=['user', 'item'],
                                               name='unique_rating')]

    def __str__(self):
        return str(self.star)
