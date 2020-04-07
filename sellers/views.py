# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from accounts.forms import ContactUsForm
from inventory.models import Inventory, Categories
from sellers.forms import *
from sellers.models import *
from shop.forms import SubscribeForm, SearchForm
from shop.models import Cart
from staffapp.models import ContactMessages


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
    return redirect('shop:searchLocation')


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


def store_products(request, hash):
    store = Stores.objects.get(hash=hash)
    subscribe_form = SubscribeForm()
    search_form = SearchForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    new_products = Inventory.objects.filter(owner=store).order_by('-time_added')[:4]
    fruits = Inventory.objects.filter(category=Categories.objects.get(name__contains='fruits'), owner=store).order_by(
        'time_added')[
             :4]
    vegies = Inventory.objects.filter(category=Categories.objects.get(name__contains='vegetables'),
                                      owner=store).order_by(
        'time_added')[:4]
    spices = Inventory.objects.filter(category=Categories.objects.get(name__contains='spice'), owner=store).order_by(
        'time_added')[
             :4]
    household = Inventory.objects.filter(category=Categories.objects.get(name__contains='household'),
                                         owner=store).order_by(
        'time_added')[:4]
    cereals = Inventory.objects.filter(category=Categories.objects.get(name__contains='cereals'), owner=store).order_by(
        'time_added')[:4]
    sanitisers = Inventory.objects.filter(category=Categories.objects.get(name__contains='sanitizers'),
                                          owner=store).order_by(
        'time_added')[:4]
    return render(request, 'shopeaze/shop_products.html',
                  {'fruits': fruits, 'vegetables': vegies, 'spices': spices, 'household_items': household,
                   'cereals': cereals, 'sanitizers': sanitisers, 'new_products': new_products, 'cart_count': cart_items,
                   'subscribe_form': subscribe_form, 'search_form': search_form, 'store': store})


def about(request):
    subscribe_form = SubscribeForm()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        return render(request, 'shopeaze/about_seller.html',
                      {'cart_count': cart_items, 'subscribe_form': subscribe_form})


def contact(request):
    subscribe_form = SubscribeForm()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            sender_mail = form.cleaned_data['sender_mail']
            sender_name = form.cleaned_data['sender_name']
            message = "From:" + sender_name + form.cleaned_data['mail_message']
            subject = form.cleaned_data['mail_subject']
            # EmailMessage()
            # todo change domain
            send_mail(from_email=sender_mail, recipient_list=['info@shopeaze.com'], subject=subject,
                      message=message)
            new_msg = ContactMessages.objects.create(sender_mail=sender_mail, sender_name=sender_name,
                                                     mail_message=message, mail_subject=subject)
            return redirect('shop:contact-us')

    return render(request, 'shopeaze/contact_seller.html',
                  {'cart_count': cart_items, 'form': form, 'subscribe_form': subscribe_form})
