# Generated by Django 3.0.3 on 2020-04-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mpesa_api', '0005_auto_20200417_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesapayment',
            name='amount',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mpesapayment',
            name='organization_balance',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
