# Generated by Django 2.2.3 on 2019-07-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_itemrental'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('S', 'success'), ('P', 'primary'), ('I', 'info'), ('W', 'warning'), ('D', 'danger'), ('A', 'dark'), ('S', 'secondary'), ('L', 'light')], default='P', max_length=1),
        ),
    ]
