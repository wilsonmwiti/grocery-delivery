from django.conf.urls import url

from . import views

app_name = 'staff'
urlpatterns = [
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^add-items/$', views.additems, name='additems'),
    url(r'^view-sales/$', views.sales, name='branch_sales'),
    url(r'^view-orders/$', views.orders, name='branch_orders'),
    url(r'^view-messages/$', views.messages, name='branch_messages'),
    url(r'^view-reports/$', views.reports, name='branch_reports'),
    # end of authentication for website

]
