from django.contrib import admin

# Register your models here.
from mpesa_api.models import MpesaPayment


class MpesaPaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'reference', 'customer', 'amount', 'order_id', 'merchant_request_id',
        'CheckoutRequestID', 'ResultDesc',
        'TransactionDate', 'phone_number',)
    search_fields = ('amount', 'reference', 'order_id')
    # fields = []
    readonly_fields = ['customer', 'amount', 'reference', 'order_id', 'merchant_request_id',
                       'CheckoutRequestID', 'ResultDesc',
                       'TransactionDate', 'phone_number']


admin.site.register(MpesaPayment, MpesaPaymentsAdmin)
