from django.conf.urls import url

from . import views

app_name = 'payments'
urlpatterns = [
    url(r'^Cash_Order_created/$', views.cash_payments_done, name='payments-cash-done'),
    url(r'^cash-payments-checkout/$', views.cash_payments, name='payments-cash'),

    # end of authentication for website

]
