# Generated by Django 3.0.3 on 2020-02-22 15:34

import django_cryptography.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_auto_20200222_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=20)),
        ),
    ]