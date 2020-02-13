from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts.forms import UserLoginForm
from . import views

app_name = 'payments'
urlpatterns = [
    url(r'^payments/$', views.payments_home, name='payments_home'),

    # end of authentication for website

]
