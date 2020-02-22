from django.contrib import admin

# Register your models here.
from staffapp.models import *

# class Payments_admin(admin.ModelAdmin):
#     list_display = ()
admin.site.register(Payments)
admin.site.register(Sales)
