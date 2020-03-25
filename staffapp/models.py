from django.db import models

from accounts.models import User
# Create your models here.
from inventory.models import Inventory


class Payments(models.Model):
    reference_number = models.CharField(max_length=500)
    payment_mode = models.CharField(max_length=500)
    time_added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        db_table = "payments"
        verbose_name_plural = "payments"


class Sales(models.Model):
    time_sold = models.DateTimeField(auto_now_add=True)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(Inventory, blank=True)

    class Meta:
        db_table = 'sales'
        verbose_name_plural = 'sales'
