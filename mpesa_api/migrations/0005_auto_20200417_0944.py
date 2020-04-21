# Generated by Django 3.0.3 on 2020-04-17 09:44

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mpesa_api', '0004_auto_20200417_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpesapayment',
            old_name='description',
            new_name='CheckoutRequestID',
        ),
        migrations.RenameField(
            model_name='mpesapayment',
            old_name='type',
            new_name='ResultDesc',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='mpesapayment',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='TransactionDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='merchant_request_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='mpesapayment',
            name='order_id',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]