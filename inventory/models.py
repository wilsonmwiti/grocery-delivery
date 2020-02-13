from django.db import models


# Create your models here.
# model for categories
class Categories(models.Model):
    name = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"


# model for inventory items
class Inventory(models.Model):
    item_name = models.CharField(max_length=20)
    price_per_kg = models.CharField(max_length=20)
    contents = models.TextField(max_length=20000)
    delivery = models.BooleanField(default=False)
    amount_remaining = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "inventory items"
