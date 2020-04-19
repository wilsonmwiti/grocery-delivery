from django.db import models
from django.utils.crypto import get_random_string

from accounts.models import User
from payments.models import PaymentsBaseModel


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# M-pesa Payment models

class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'


class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'


class MpesaPayment(BaseModel, PaymentsBaseModel):
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

    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        self.order_id = get_random_string(length=9)
        super(MpesaPayment, self).save(*args, **kwargs)
