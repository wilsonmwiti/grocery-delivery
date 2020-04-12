from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    url('wishlist/', views.wishlist, name='wishlist'),
    url('remove-from-wishes/(?P<pk>[0-9]+)/$', views.delete_wish, name='delete-wish'),
    url('add-to-wishes/(?P<pk>[0-9a-zA-Z]+)/$', views.add_wish, name='add-wish'),
    url('product/(?P<hash>[0-9a-zA-Z]+)/$', views.product, name='product-single'),
    url('category/(?P<storehash>[0-9a-zA-Z]+)/(?P<categorypk>[0-9]+)$', views.categories, name='category-products'),
    url('cart/', views.cart, name='cart'),
    # url('add-to-order/(?P<pk>[0-9]+)/$', views.add_to_cart, name='orderadd'),
    url('cuppyadd/(?P<pk>[0-9]+)/$', views.cuppy_add, name='cuppyorderinclude'),
    # for anything that does not require size as input suc as cup cakes
    url('add/(?P<pk>[0-9]+)/$', views.single_add, name='single-product-add'),
    # for anything that does not require size as input suc as cup cakes
    url('remove-from-order/(?P<pk>[0-9]+)/$', views.remove_from_cart, name='remove'),
    url('check-out/', views.checkout, name='checkout'),
    url('about-us/', views.about, name='about-us'),
    url('contact-us/', views.contact, name='contact-us'),
    url('login/', views.login, name='login'),
    url('subscribe/', views.subscribe, name='subscribe'),
    url('search/', views.search, name='search'),
    url('searchStores/', views.searchstores, name='searchLocation'),

    # end of authentication for website

]
