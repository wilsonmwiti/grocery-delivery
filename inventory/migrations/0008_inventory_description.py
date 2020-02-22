# Generated by Django 3.0.3 on 2020-02-22 16:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0007_inventory_discounted_price_per_kg'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
