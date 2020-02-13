from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts.forms import UserLoginForm
from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^inventory/$', views.login, name='login'),

    # end of authentication for website

]
