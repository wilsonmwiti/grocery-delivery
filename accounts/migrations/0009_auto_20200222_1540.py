# Generated by Django 3.0.3 on 2020-02-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0008_auto_20200222_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
