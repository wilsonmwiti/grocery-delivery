# Generated by Django 3.0.3 on 2020-04-05 12:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sellers', '0003_auto_20200402_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]