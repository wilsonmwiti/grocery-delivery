from django.conf.urls import url

from . import views

app_name = 'staff'
urlpatterns = [
    url(r'^panel/$', views.panel, name='panel'),
    # end of authentication for website

]
