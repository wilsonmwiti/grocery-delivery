# Generated by Django 3.0.3 on 2020-04-17 06:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('mpesa_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MpesaCallBacks',
        ),
        migrations.DeleteModel(
            name='MpesaCalls',
        ),
        migrations.DeleteModel(
            name='MpesaPayment',
        ),
    ]
