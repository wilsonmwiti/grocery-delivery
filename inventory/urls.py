from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^inventory/$', views.login, name='login'),

    # end of authentication for website

]
