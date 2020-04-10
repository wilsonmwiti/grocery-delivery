# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

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
        user = User.objects.get(pk=request.user.pk)
        line = StoreLine.objects.filter(admin=user)
        stores = Stores.objects.filter(line__admin=user)
        user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller')
        store_line_form = StoresLineCreationForm()
        stores_form = StoresCreationForm()
        return render(request, 'shopeaze/seller-panel/panel-home.html',
                      {'line': line, 'stores': stores, 'StoreLineForm': store_line_form, 'StoresForm': stores_form,
                       'seller': user_is_seller})

    else:
        return HttpResponse('<p>hey</p>')


def list(request):
    return redirect('shop:searchLocation')


def add_line(request):
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
            new_store = Stores.objects.create(line=line, town=town,
                                              phone_number=phone_number, email=email)

        else:
            print(form.errors)
    return redirect('sellers:panel')


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
    new_products = Inventory.objects.filter(owner=store).order_by('-time_added')[:8]
    context_items = {}

    fruits = Inventory.objects.filter(category=Categories.objects.get(name__contains='fruits'), owner=store).order_by(
        'time_added')[
             :8]
    if fruits.count() > 0:
        context_items['fruits'] = fruits
    vegies = Inventory.objects.filter(category=Categories.objects.get(name__contains='vegetables'),
                                      owner=store).order_by(
        'time_added')[:8]
    if vegies.count() > 0:
        context_items['vegetables'] = vegies
    spices = Inventory.objects.filter(category=Categories.objects.get(name__contains='spice'), owner=store).order_by(
        'time_added')[
             :8]
    if spices.count() > 0:
        context_items['spices'] = spices
    household = Inventory.objects.filter(category=Categories.objects.get(name__contains='household'),
                                         owner=store).order_by(
        'time_added')[:8]
    if household.count() > 0:
        context_items['household_items'] = household
    cereals = Inventory.objects.filter(category=Categories.objects.get(name__contains='cereals'), owner=store).order_by(
        'time_added')[:8]
    if cereals.count() > 0:
        context_items['cereals'] = cereals
    sanitisers = Inventory.objects.filter(category=Categories.objects.get(name__contains='sanitizers'),
                                          owner=store).order_by(
        'time_added')[:8]
    if sanitisers.count() > 0:
        context_items['sanitizers'] = sanitisers
    context_forms = {'cart_count': cart_items,
                     'subscribe_form': subscribe_form, 'search_form': search_form, 'store': store}
    context_items['new_products'] = new_products
    context_items.update(context_forms)
    return render(request, 'shopeaze/shop_products.html',
                  context_items)


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


def update_store(request):
    if request.method == 'POST':
        store = request.POST.get('store')
        number = request.POST.get('number')
        email = request.POST.get('email')
        admin = request.POST.get('admin')
        adminobj = User.objects.get(email=admin)
        current_site = get_current_site(request)
        subject = 'Request to be a  store admin'
        message = render_to_string('shopeaze/seller-panel/admin_activation_email.html', {
            'user': adminobj,
            'domain': current_site.domain,
            'token': adminobj.hash
        })
        send_mail(
            subject,
            message,
            'info@nanotechsoftwares.co.ke',
            [adminobj.__str__()],
            fail_silently=False,
        )
        storename = request.POST.get('store')
        store_object = Stores.objects.filter(pk=store)
        for obj in store_object:
            obj.email = email
            obj.name = storename
            obj.admin = adminobj
            obj.phone_number = number
            obj.save()

    return redirect('sellers:panel')


def setmanager(request, hash):
    print("hello!!")
    adminobj = User.objects.get(hash=hash)
    if adminobj:
        adminobj.user_type = 'staff'
        adminobj.save()
    return redirect('sellers:activationsuccessfull')


def activation_successful(request):
    subscribe_form = SubscribeForm()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    form = ContactUsForm()
    return render(request, 'shopeaze/success.html',
                  {'cart_count': cart_items, 'form': form, 'subscribe_form': subscribe_form})
