# Create your views here.
from django.shortcuts import render

from shop.models import Orders
from shop.views import create_order


def payments_home(request):
    return None


def cash_payments(request):
    return render(request, 'shopeaze/payments/cash-confirmation.html')


def cash_payments_done(request):
    order = Orders.objects.create()
    create_order(request=request, mode='CASH')
    return render(request, 'shopeaze/payments/order-done.html')
