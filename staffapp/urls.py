from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts.forms import UserLoginForm
from . import views

app_name = 'staff'
urlpatterns = [
    url(r'^staff-app/$', views.login, name='login_staff'),
    # end of authentication for website

]
