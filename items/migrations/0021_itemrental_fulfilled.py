# Generated by Django 2.2.3 on 2019-07-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0020_auto_20190729_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemrental',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
    ]