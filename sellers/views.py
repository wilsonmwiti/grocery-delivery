# Create your views here.
from django.shortcuts import render, redirect

from inventory.models import Inventory
from sellers.forms import *
from sellers.models import *
from shop.forms import SubscribeForm, SearchForm
from shop.models import Cart


def panel(request):
    user = User.objects.get(pk=request.user.pk)
    line = StoreLine.objects.filter(admin=user)
    stores = Stores.objects.filter(line=line)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller')

    if line.count() > 0:

        return render(request, 'shopeaze/seller-panel/panel-home.html',
                      {'line': line, 'stores': stores, 'seller': user_is_seller})
    else:
        store_line_form = StoresLineCreationForm()
        stores_form = StoresCreationForm()
        return render(request, 'shopeaze/seller-panel/panel-profile.html',
                      {'line': line, 'stores': stores, 'StoreLineForm': store_line_form,
                       'StoresForm': stores_form, 'seller': user_is_seller})


def profile(request):
    user = User.objects.get(pk=request.user.pk)
    line = StoreLine.objects.filter(admin=user)
    stores = Stores.objects.filter(line=line)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller')
    store_line_form = StoresLineCreationForm()
    stores_form = StoresCreationForm()
    return render(request, 'shopeaze/seller-panel/panel-profile.html',
                  {'line': line, 'stores': stores, 'StoreLineForm': store_line_form, 'StoresForm': stores_form,
                   'seller': user_is_seller})


def list(request):
    return redirect('shop:searchlocation')


def addline(request):
    if request.method == 'POST':
        form = StoresLineCreationForm(request.POST, request.FILES)
        if form.is_valid():
            line_name = form.cleaned_data['name']
            logo = form.cleaned_data['logo']
            description = form.cleaned_data['description']
            user = User.objects.get(pk=request.user.pk)
            newstoreline = StoreLine.objects.create(name=line_name, description=description, logo=logo, admin=user)
        else:
            print(form.errors)
    return redirect('sellers:profile')


def addStore(request):
    if request.method == 'POST':
        form = StoresCreationForm(request.POST, request.FILES)
        if form.is_valid():
            town = form.cleaned_data['town']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            user = User.objects.get(pk=request.user.pk)
            line = StoreLine.objects.get(admin=user)
            new_store = Stores.objects.create(line=line, name='{0} {1}'.format(line.name, town), town=town,
                                              phone_number=phone_number, email=email)
        else:
            print(form.errors)
    return redirect('sellers:profile')


def sales(request):
    return None


def reports(request):
    return None


def messages(request):
    return None


def orders(request):
    return None


def store_products(request, pk):
    store = Stores.objects.get(pk=pk)
    items = Inventory.objects.filter(owner=store).order_by('id')[:12]
    subscribe_form = SubscribeForm()
    search_form = SearchForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    new_products = Inventory.objects.filter(owner=store).order_by('-time_added')[:4]

    return render(request, 'shopeaze/shop_products.html',
                  {'products': items, 'new_products': new_products, 'cart_count': cart_items,
                   'subscribe_form': subscribe_form, 'search_form': search_form})
