from django.contrib import admin

# Register your models here.
from shop.models import *


class OrdersAdmin(admin.ModelAdmin):
    list_display = ['store', 'user', 'order_string', 'payment_mode']
    search_fields = ['order_string', 'payment_mode']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity']


admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
admin.site.register(PartiallyPaid)
