from math import ceil

from django.db import models

# Create your models here.
from accounts.models import User
from inventory.models import Inventory


class PartiallyPaid(models.Model):
    time_added = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    current_paid_amount = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)

    class Meta:
        db_table = 'partial_payments'
        verbose_name_plural = 'PartialPayments'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    time_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Carts'
        db_table = 'Cart'

    def save(self, *args, **kwargs):
        # fixme error in discount calculation
        try:
            if not self.item.discounted:
                self.price = ceil(float(self.item.price_per_unit) * self.qty)
                self.unit_price = self.item.price_per_unit
            else:
                self.price = ceil(float(self.item.discounted_price_per_unit) * self.qty)
                self.unit_price = self.item.discounted_price_per_unit
        except ZeroDivisionError:
            pass
        super(Cart, self).save(*args, **kwargs)
