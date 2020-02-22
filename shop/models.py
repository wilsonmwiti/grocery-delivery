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

    class Meta:
        verbose_name_plural = 'Carts'
        db_table = 'Cart'
