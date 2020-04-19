from django.contrib import admin

# Register your models here.
from mpesa_api.models import MpesaPayment


class MpesaPaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'reference', 'customer', 'amount', 'order_id', 'merchant_request_id',
        'CheckoutRequestID', 'ResultDesc',
        'TransactionDate', 'phone_number', 'confirmation_status')
    search_fields = ('amount', 'reference', 'order_id')
    # fields = []
    readonly_fields = ['customer', 'amount', 'reference', 'order_id', 'merchant_request_id',
                       'CheckoutRequestID', 'ResultDesc',
                       'TransactionDate', 'phone_number']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(MpesaPayment, MpesaPaymentsAdmin)
