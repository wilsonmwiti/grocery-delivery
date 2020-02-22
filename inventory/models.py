from math import ceil

from django.db import models
# Create your models here.
# model for categories
from django.utils.safestring import mark_safe


class Categories(models.Model):
    name = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
# model for inventory items
class Inventory(models.Model):
    item_name = models.CharField(max_length=20)
    price_per_kg = models.CharField(max_length=20)
    discounted_price_per_kg = models.CharField(max_length=20)
    egg_less = models.BooleanField(default=True)
    delivery = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    amount_remaining = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    discounted = models.BooleanField(default=False)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "inventory items"

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.image.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        self.discounted_price_per_kg = ceil(float(self.price_per_kg) - float(self.price_per_kg) / self.discount)
        super(Inventory, self).save(*args, **kwargs)
