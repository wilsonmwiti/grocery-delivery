# Register your models here.
from django.contrib import admin

# the module name is app_name.models
from inventory.models import Categories, Inventory


# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_added', 'unit',)
    search_fields = ('name',)


class InventoryAdmin(admin.ModelAdmin):
    # item_name = models.CharField(max_length=20)
    #     price_per_kg = models.CharField(max_length=20)
    #     contents = models.TextField(max_length=20000)
    #     delivery = models.BooleanField(default=False)
    #     amount_remaining = models.CharField(max_length=20)
    #     time_added = models.DateTimeField(auto_now_add=True)
    #     category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    list_display = (
        'id', 'item_name', 'price_per_unit', 'image_tag', 'category',
        'discount', 'discounted_price_per_unit',
        'discounted', 'offer_of_the_day',)
    search_fields = ('item_name', 'description', 'hash')
    # fields = []
    readonly_fields = ['image_tag', 'discounted_price_per_unit', 'hash']


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Inventory, InventoryAdmin)
