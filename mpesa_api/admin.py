from django.contrib import admin

# Register your models here.
from mpesa_api.models import MpesaPayment

admin.site.register(MpesaPayment)
