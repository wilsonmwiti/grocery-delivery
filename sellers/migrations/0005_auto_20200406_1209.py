# Generated by Django 3.0.3 on 2020-04-06 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sellers', '0004_stores_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='openinghours',
            table='hours',
        ),
    ]
