# Generated by Django 3.0.3 on 2020-04-06 19:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sellers', '0007_auto_20200406_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='hash',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
