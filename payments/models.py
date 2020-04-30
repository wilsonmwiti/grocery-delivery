from django.db import models
from django.utils.crypto import get_random_string

from accounts.models import User


class PaymentsBaseModel(models.Model):
    confirmation_status = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CashPayment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_id = models.CharField(null=True, max_length=3000)
    amount = models.CharField(max_length=10, null=True)
    reference = models.TextField(null=True)
    merchant_request_id = models.TextField(null=True)
    CheckoutRequestID = models.TextField(null=True)
    ResultDesc = models.TextField(null=True)
    TransactionDate = models.DateTimeField(auto_now_add=True)
    phone_number = models.TextField(null=True)
    organization_balance = models.CharField(max_length=10, null=True)
    confirmation_status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Cash Payment'
        verbose_name_plural = 'Cash Payments'

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        self.order_id = get_random_string(length=9)
        super(CashPayment, self).save(*args, **kwargs)
