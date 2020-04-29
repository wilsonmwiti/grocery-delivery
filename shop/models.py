from django.db import models

# Create your models here.
from accounts.models import User
from inventory.models import Inventory
from sellers.extras import encrypt_string
from sellers.models import Stores


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
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    time_added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0)
    size = models.CharField(null=True, default=None, max_length=20)
    hash = models.TextField()

    class Meta:
        verbose_name_plural = 'Carts'
        db_table = 'Cart'

    def save(self, *args, **kwargs):
        # fixme error in discount calculation
        try:
            self.hash = encrypt_string('{}'.format(self.pk))
            if not self.item.discounted:
                self.price = float(self.item.price_per_unit) * float(self.qty)
                self.unit_price = float(self.item.price_per_unit)
            else:
                self.price = float(self.item.discounted_price_per_unit) * float(self.qty)
                self.unit_price = float(self.item.discounted_price_per_unit)
        except ZeroDivisionError:
            pass
        super(Cart, self).save(*args, **kwargs)

    # def update(self, *args, **kwargs):
    #     # fixme error in discount calculation
    #     try:
    #         if not self.item.discounted:
    #             self.price = float(self.item.price_per_unit) * float(self.qty)
    #             self.unit_price = float(self.item.price_per_unit)
    #         else:
    #             self.price = float(self.item.discounted_price_per_unit) * float(self.qty)
    #             self.unit_price = float(self.item.discounted_price_per_unit)
    #     except ZeroDivisionError:
    #         pass
    #     super(Cart, self).update(*args, **kwargs)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)

    # price = models.IntegerField(default=0)
    # unit_price = models.IntegerField(default=0)

    class Meta:
        db_table = "wishlist"
        verbose_name_plural = 'Wish Lists'

    def save(self, *args, **kwargs):
        # fixme error in discount calculation
        try:
            if not self.item.discounted:
                self.unit_price = float(self.item.price_per_unit)
            else:
                self.unit_price = float(self.item.discounted_price_per_unit)
        except ZeroDivisionError:
            pass
        super(WishList, self).save(*args, **kwargs)


class Orders(models.Model):
    store = models.ForeignKey(Stores, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_string = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20)
    fulfilled = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'
        verbose_name_plural = 'orders'


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.CharField(max_length=10)
    # checklist=models.BooleanField(default=False)


class CustomerData(models.Model):
    # todo come up with an analysis model of the items in this table
    # for trying to come up with a prediction of customer
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    item_name = models.CharField(max_length=200)
    action = models.CharField(max_length=20)
    time_of_action = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'prediction'
