# Generated by Django 2.2.3 on 2019-07-29 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20190729_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(default='item_pictures/default.jpg', upload_to='item_pictures'),
        ),
    ]
