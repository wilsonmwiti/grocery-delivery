# Generated by Django 3.0.3 on 2020-02-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0005_auto_20200222_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inventory',
            name='discounted',
            field=models.BooleanField(default=False),
        ),
    ]