# Generated by Django 3.2.12 on 2022-03-25 21:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20220325_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag'),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=100, help_text='max 32767 ,min 1', validators=[django.core.validators.MaxValueValidator(32767), django.core.validators.MinValueValidator(1)], verbose_name='Вес'),
        ),
    ]