# Generated by Django 3.2.12 on 2022-03-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.IntegerField(help_text='1-5', verbose_name='Оценка'),
        ),
    ]