# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from accounts.forms import ContactUsForm
from inventory.models import Inventory, Categories
from sellers.extras import split_domain_ports
from sellers.forms import *
from sellers.models import *
from shop.forms import SubscribeForm, SearchForm, SearchOrderForm
from shop.models import Cart, Orders
from staffapp.models import ContactMessages


@login_required(login_url='customer-accounts:login')
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
        return HttpResponse('<p>Contact Administrator For A Line To Be Created For You</p>')


@login_required(login_url='customer-accounts:login')
def list(request):
    return redirect('shop:searchLocation')


@login_required(login_url='customer-accounts:login')
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


@login_required(login_url='customer-accounts:login')
def addStore(request):
    if request.method == 'POST':
        form = StoresCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(pk=request.user.pk)
            line = StoreLine.objects.get(admin=user)
            store = form.save(commit=False)
            store.line = line
            store.save()

        else:
            print(form.errors)
    return redirect('sellers:panel')


@login_required(login_url='customer-accounts:login')
def sales(request):
    # user = User.objects.get(pk=request.user.pk)
    # stores = Stores.objects.get(admin=user)
    # search_form = SearchForm()
    #
    # line = StoreLine.objects.get(pk=stores.line.pk)
    # order = Orders.objects.get(pk=pk)
    # order_items = OrderItems.objects.filter(order=order)
    # # if request.method=='POST':
    #
    # return render(request, 'shopeaze/staff-panel/view_orders.html',
    #               {'line': line, 'order_items': order_items, 'search_form': search_form, 'order': order
    #                })
    pass


@login_required(login_url='customer-accounts:login')
def reports(request):
    return None


@login_required(login_url='customer-accounts:login')
def messages(request):
    return None


@login_required(login_url='customer-accounts:login')
def orders(request):
    user = User.objects.get(pk=request.user.pk)
    search_form = SearchOrderForm()

    line = StoreLine.objects.get(admin=user)
    orders = Orders.objects.filter(store__line=line)
    if request.method == 'POST':
        search_form = SearchOrderForm(request.POST)
        if search_form.is_valid():
            order_id = search_form.cleaned_data['order_id']
            orders = Orders.objects.filter(store__line=line, order_string__exact=order_id)
    return render(request, 'shopeaze/seller-panel/line/view_orders.html',
                  {'line': line, 'search_form': search_form, 'orders': orders, 'user': user
                   })


@login_required(login_url='customer-accounts:login')
def store_products(request, hash):
    user = User.objects.get(pk=request.user.pk)
    store = Stores.objects.get(hash=hash)
    subscribe_form = SubscribeForm()
    search_form = SearchForm()
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    new_products = Inventory.objects.filter(owner=store).order_by('-time_added')[:8]
    categories = Categories.objects.all().order_by('name')
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

    context_items['categories'] = categories
    context_items['store'] = store
    context_items['initials'] = ''.join([x[0] for x in store.name.split()])
    context_items['cart_count'] = Cart.objects.filter(user=user).count()
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

            send_mail(from_email=sender_mail, recipient_list=['info@' + split_domain_ports(request.get_host()),
                                                              ], subject=subject,
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
            'info@' + split_domain_ports(request.get_host()),
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


def cancel_order(request, pk):
    order = Orders.objects.get(pk=pk)
    customer = order.user.email
    store = order.store.name
    store_email = order.store.email
    send_mail("{} order cancelled".format(store), "Your order from {} has been cancelled".format(store), store_email,
              [customer, order.store.admin.email, 'info@' + split_domain_ports(request.get_host()),
               ])
    order = Orders.objects.filter(pk=pk).delete()
    return redirect('sellers:line_orders')
