# Generated by Django 3.0.3 on 2020-03-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0003_auto_20200325_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='discounted_price_per_unit',
            field=models.IntegerField(),
        ),
    ]
