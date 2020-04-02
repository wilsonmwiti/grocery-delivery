from math import ceil

from django.db import models
# Create your models here.
# model for categories
from django.utils.safestring import mark_safe

from sellers.models import Stores


class Categories(models.Model):
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# model for inventory items
class Inventory(models.Model):
    owner = models.ForeignKey(Stores, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20)
    price_per_unit = models.CharField(max_length=20)
    discounted_price_per_unit = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    time_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    discounted = models.BooleanField(default=False)
    offer_of_the_day = models.BooleanField(default=False)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "inventory items"

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.image.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        try:
            self.discounted_price_per_unit = ceil(
                float(self.price_per_unit) - float(self.price_per_unit) / self.discount)
        except ZeroDivisionError:
            pass
        super(Inventory, self).save(*args, **kwargs)
