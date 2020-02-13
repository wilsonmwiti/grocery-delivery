from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.forms import UserLoginForm
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='account_activation_sent'),

    # end of authentication for website

]
