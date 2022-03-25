# Generated by Django 3.2.12 on 2022-03-25 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20220326_0023'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0002_auto_20220325_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(choices=[(1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')], default=0, verbose_name='Оценка'),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='unique_rating'),
        ),
    ]
