from django.contrib import admin

# Register your models here.
from shop.models import PartiallyPaid, Cart

admin.site.register(PartiallyPaid)
admin.site.register(Cart)
