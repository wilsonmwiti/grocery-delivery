from math import ceil

from django.db import models

# Create your models here.
from accounts.models import User
from inventory.models import Inventory


class PartiallyPaid(models.Model):
    pass
    # sales_id
    # class Meta:
    #     db_table='partial payments'
    #     verbose_name_plural='PartialPayments'


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
        try:
            if not self.item.discounted:
                self.price = ceil(float(self.item.price_per_kg) * self.qty)
                self.unit_price = self.item.price_per_kg
            else:
                self.price = ceil(float(self.item.discounted_price_per_kg) * self.qty)
                self.unit_price = self.item.discounted_price_per_kg
        except ZeroDivisionError:
            pass
        super(Cart, self).save(*args, **kwargs)
