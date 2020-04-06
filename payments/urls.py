from django.conf.urls import url

from . import views

app_name = 'payments'
urlpatterns = [
    url(r'^payments/$', views.payments_home, name='payments_home'),

    # end of authentication for website

]
