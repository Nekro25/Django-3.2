# Generated by Django 3.2.12 on 2022-04-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_auto_20220326_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(choices=[(None, '----'), (1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь')], default=0, null=True, verbose_name='Оценка'),
        ),
    ]
