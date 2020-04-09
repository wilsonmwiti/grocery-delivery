from django.conf.urls import url

from . import views

app_name = 'sellers'
urlpatterns = [

    url(r'^panel/$', views.panel, name='panel'),
    url(r'^add-line/$', views.add_line, name='add_line'),
    url(r'^add-store/$', views.addStore, name='addstore'),
    url(r'^line-sales/$', views.sales, name='line_sales'),
    url(r'^line-reports/$', views.reports, name='line_reports'),
    url(r'^line-messages/$', views.messages, name='line_messages'),
    url(r'^line-orders/$', views.orders, name='line_orders'),
    url(r'^list/$', views.list, name='list'),
    url(r'^store/(?P<hash>[0-9a-zA-Z]+)/$', views.store_products, name='store'),
    url('about-us/', views.about, name='about-us'),
    url('contact-us/', views.contact, name='contact-us'),
    url('update-store/', views.update_store, name='updatestore'),
]
