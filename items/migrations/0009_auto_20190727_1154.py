# Generated by Django 2.2.3 on 2019-07-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20190727_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
