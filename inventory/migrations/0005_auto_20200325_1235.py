# Generated by Django 3.0.3 on 2020-03-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0004_auto_20200325_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='discounted_price_per_unit',
            field=models.CharField(max_length=20),
        ),
    ]
