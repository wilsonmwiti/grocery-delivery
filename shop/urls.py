from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    url('wishlist/', views.wishlist, name='wishlist'),
    url('product/(?P<pk>[0-9]+)/$', views.product, name='product-single'),
    url('cart/', views.cart, name='cart'),
    url('check-out/', views.checkout, name='checkout'),
    url('about-us/', views.about, name='about-us'),
    url('contact-us/', views.contact, name='contact-us'),
    url('login/', views.login, name='login'),

    # end of authentication for website

]
