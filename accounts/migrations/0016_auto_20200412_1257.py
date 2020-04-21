# Generated by Django 3.0.3 on 2020-04-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0015_auto_20200412_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='alternative_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile_money_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]