from django.conf.urls import url

from . import views

app_name = 'sellers'
urlpatterns = [

    url(r'^panel/$', views.panel, name='panel'),
    url(r'^list/$', views.list, name='list'),

]
