from django.conf.urls import url

from . import views

app_name = 'staff'
urlpatterns = [
    url(r'^staff-app/$', views.login, name='login_staff'),
    # end of authentication for website

]
