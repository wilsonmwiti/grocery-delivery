# Generated by Django 3.0.3 on 2020-03-25 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0004_auto_20200325_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='ordered',
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table='wishlist',
        ),
    ]
