# Generated by Django 2.2.3 on 2019-07-27 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20190727_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
        ),
    ]
