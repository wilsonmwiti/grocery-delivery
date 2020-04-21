from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django_cryptography.utils.crypto import get_random_string

from accounts.forms import ContactUsForm
from accounts.models import User, Profile
from inventory.models import Inventory, Categories
from mpesa_api.models import MpesaPayment
from sellers.models import Stores
from shop.forms import QuantityForm, QuantityFormCuppy, SubscribeForm, SearchForm, SearchStoresForm, PaymentsForm
from shop.models import Cart, WishList, Orders, OrderItems
from staffapp.models import ContactMessages, Subscribers


def index(request):
    subscribe_form = SubscribeForm()
    search_form = SearchStoresForm()
    products = Inventory.objects.all().order_by('id')[:12]
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    fruits = Inventory.objects.filter(category=Categories.objects.get(name__contains='fruits')).order_by('time_added')[
             :4]
    vegies = Inventory.objects.filter(category=Categories.objects.get(name__contains='vegetables')).order_by(
        'time_added')[:4]
    spices = Inventory.objects.filter(category=Categories.objects.get(name__contains='spice')).order_by('time_added')[
             :4]
    household = Inventory.objects.filter(category=Categories.objects.get(name__contains='household')).order_by(
        'time_added')[:4]
    cereals = Inventory.objects.filter(category=Categories.objects.get(name__contains='cereals')).order_by(
        'time_added')[:4]
    sanitisers = Inventory.objects.filter(category=Categories.objects.get(name__contains='sanitizers')).order_by(
        'time_added')[:4]
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    user_is_staff = User.objects.filter(pk=request.user.pk, user_type='staff').count()

    if user_is_seller > 0:
        return redirect('sellers:panel')
    elif user_is_staff > 0:
        return redirect('staff:panel')
    else:
        stores = Stores.objects.all()
        return render(request, 'shopeaze/index.html',
                      {'products': products, 'fruits': fruits, 'vegetables': vegies, 'spices': spices,
                       'household_items': household, 'cereals': cereals, 'sanitizers': sanitisers,
                       'cart_count': cart_items,
                       'subscribe_form': subscribe_form, 'formSearchShop': search_form, 'stores': stores})


@login_required(login_url='customer-accounts:login')
def add_wish(request, hash):
    print("in wishes")
    user = User.objects.get(pk=request.user.pk)
    wishobj = WishList.objects.filter(user=user)
    item = Inventory.objects.get(hash=hash)
    if wishobj:
        print("user has wishes")
        # if users wishlist exists
        obj = WishList.objects.filter(user=user, item=item)
        if obj:
            #     if object exists in wishlist
            pass
        else:
            print("create objects in wishes")
            # object does not exist in wishlist
            wishobj = WishList.objects.create(user=user, item=item)

    else:
        # user wishlist does not exist
        print("create user wishes and add wish")
        wishobj = WishList.objects.create(user=user, item=item)
    return redirect("shop:index")


@login_required(login_url='customer-accounts:login')
def delete_wish(request, hash):
    user = User.objects.get(pk=request.user.pk)
    item = Inventory.objects.get(hash=hash)
    remove_item = WishList.objects.filter(user=user, item=item)
    remove_item.delete()

    return redirect("shop:wishlist")


@login_required(login_url='customer-accounts:login')
def wishlist(request):
    subscribe_form = SubscribeForm()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    wishes = WishList.objects.filter(user=request.user.pk)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        return render(request, 'shopeaze/wishlist.html',
                      {'wishes': wishes, 'cart_count': cart_items, 'subscribe_form': subscribe_form})


def product(request, hash):
    subscribe_form = SubscribeForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    form = QuantityForm()
    product_details = get_object_or_404(Inventory, hash=hash)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        return render(request, 'shopeaze/product-single.html',
                      {'product': product_details, 'form': form, 'cart_count': cart_items,
                       'subscribe_form': subscribe_form})


# 198919
@login_required(login_url='customer-accounts:login')
def cart(request):
    subscribe_form = SubscribeForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    cart = Cart.objects.filter(user=request.user.pk)
    cart_total = 0
    for x in cart:
        cart_total += x.price
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        return render(request, 'shopeaze/cart.html',
                      {'cart': cart, 'sum': cart_total, 'cart_count': cart_items, 'subscribe_form': subscribe_form})


@login_required(login_url='customer-accounts:login')
def checkout(request):
    # check if delivery profile is set and redirect to user profile creation or checkout page if it is available
    user = User.objects.get(pk=request.user.pk)
    user_profile = Profile.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)

    if user_profile.count() > 0:
        #     exists move to checkout
        subscribe_form = SubscribeForm()

        if request.user.is_authenticated:
            cart_items_count = Cart.objects.filter(user=request.user.pk).count()
        else:
            cart_items_count = 0
        payment_method_form = PaymentsForm()
        user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
        if user_is_seller > 0:
            return redirect('sellers:panel')
        else:
            cart_total = 0
            for x in cart_items:
                cart_total += x.price
            return render(request, 'shopeaze/checkout.html',
                          {'cart_count': cart_items_count, 'subscribe_form': subscribe_form, 'cart_sum': cart_total,
                           'paymentsform': payment_method_form,
                           'user': user, 'user_profile': user_profile})

    else:
        #     create profile
        return redirect('customer-accounts:createprofile')


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
        return render(request, 'shopeaze/about.html', {'cart_count': cart_items, 'subscribe_form': subscribe_form})


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

    return render(request, 'shopeaze/contact.html',
                  {'cart_count': cart_items, 'form': form, 'subscribe_form': subscribe_form})


def login(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    return redirect('customer-accounts:login')


@login_required(login_url='customer-accounts:login')
def categories(request, storehash, categorypk):
    subscribe_form = SubscribeForm()

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    owner = Stores.objects.get(hash=storehash)
    products = Inventory.objects.filter(category=categorypk, owner=owner)
    cat = get_object_or_404(Categories, pk=categorypk)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
        return render(request, 'shopeaze/categories.html',
                      {'products': products, 'cart_count': cart_items, 'category': cat,
                       'subscribe_form': subscribe_form})


@login_required(login_url='customer-accounts:login')
def remove_from_cart(request, pk):
    # removing from cart
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    user = User.objects.get(pk=request.user.pk)
    item = Inventory.objects.get(pk=pk)
    remove_item = Cart.objects.filter(user=user, item=item)
    remove_item.delete()
    return redirect('shop:cart')


@login_required(login_url='customer-accounts:login')
def cuppy_add(request, pk):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    print("cuppy add to cart")
    if request.method == 'POST':
        print("post")
        if request.user.is_authenticated:
            form = QuantityFormCuppy(request.POST)
            print(form.errors)
            if form.is_valid():

                qty = form.cleaned_data['qty']
                print("{} is the quantity".format(qty))
                user = User.objects.get(pk=request.user.pk)
                cartobj = Cart.objects.filter(user=user)
                item = Inventory.objects.get(pk=pk)

                if cartobj:
                    # if users cart exists
                    obj = Cart.objects.filter(user=user, item=item, store=item.owner)
                    if obj:
                        #     if object exists in cart
                        obj.delete()
                        cartobj = Cart.objects.create(user=user, qty=qty, item=item, store=item.owner)

                        # obj.save()
                    else:
                        # object does not exist in cart
                        cartobj = Cart.objects.create(user=user, qty=qty, item=item, store=item.owner)

                else:
                    # user cart does not exist
                    cartobj = Cart.objects.create(user=user, qty=qty, item=item, store=item.owner)
            else:
                print("invalid form")
    else:
        return redirect('shop:login')
    next = request.POST.get('next', '/')
    print("redirection")
    return HttpResponseRedirect(next)


@login_required(login_url='customer-accounts:login')
def single_add(request, pk):
    user = User.objects.get(pk=request.user.pk)
    cartobj = Cart.objects.filter(user=user)
    item = Inventory.objects.get(pk=pk)
    if cartobj:
        # if users cart exists
        obj = Cart.objects.filter(user=user, item=item, store=item.owner)
        qty = obj.model.qty + 1
        if obj:
            #     if object exists in cart
            obj.update(qty=qty)
            # obj.save()
        else:
            # object does not exist in cart
            cartobj = Cart.objects.create(user=user, qty=1, item=item)

    else:
        # user cart does not exist
        cartobj = Cart.objects.create(user=user, qty=1, item=item)
    return redirect("shop:index")


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['email']

            check_if_exists = Subscribers.objects.filter(email=mail)
            if check_if_exists:
                pass
            else:
                create_subscriber = Subscribers.objects.create(email=mail)
    next = request.POST.get('next', '/')
    print("redirection")
    return HttpResponseRedirect(next)


@login_required(login_url='customer-accounts:login')
def search(request):
    subscribe_form = SubscribeForm()
    search_form = SearchForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['item']
                items = Inventory.objects.filter(item_name__icontains=name)
                store = request.POST.get('store')
                store_details = Stores.objects.get(name__exact=store)
                return render(request, 'shopeaze/products_searched.html',
                              {'store': store_details, 'products': items, 'cart_count': cart_items,
                               'subscribe_form': subscribe_form,
                               'search_form': search_form})


def searchstores(request):
    subscribe_form = SubscribeForm()
    search_form = SearchStoresForm()
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user.pk).count()
    else:
        cart_items = 0
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller').count()
    if user_is_seller > 0:
        return redirect('sellers:panel')
    else:
        if request.method == 'POST':
            form = SearchStoresForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['store']
                items = Stores.objects.filter(town__icontains=name)

                return render(request, 'shopeaze/shops.html', {'stores': items, 'cart_count': cart_items,
                                                               'subscribe_form': subscribe_form,
                                                               'formSearchShop': search_form})
        else:
            items = Stores.objects.all()

            return render(request, 'shopeaze/shops.html', {'stores': items, 'cart_count': cart_items,
                                                           'subscribe_form': subscribe_form,
                                                           'formSearchShop': search_form})


# handles mpesa payments
@login_required(login_url='customer-accounts:login')
def payment_actions(request):
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data['payment_choices']
            if method == 'mpesastk':
                return redirect('mpesa-api:lipa_na_mpesa')
            elif method == 'cash':
                return redirect('payments:payments-cash')
            elif method == 'mpesatill':
                print('mpesa till payments')
        else:
            print(form.errors)
    else:
        print('not post')
    return None


def create_order(request=None, mode=None):
    store = None
    user = User.objects.get(pk=request.user.pk)
    cart_item_one = Cart.objects.filter(user=user)
    if cart_item_one.count() > 0:
        for x in cart_item_one:
            store = x.store

    if mode == 'MPESA':
        payment = MpesaPayment.objects.get(merchant_request_id=request.session.get('mpesa_request_id'))
        order_string = payment.order_id
    elif mode == 'CASH':
        order_string = get_random_string(length=10)
    new_order = Orders.objects.create(order_string=order_string, payment_mode=mode, store=store, user=user)
    send_mail("New Order", message='New Order:' + order_string, from_email=user.email,
              recipient_list=[store.email, store.admin.email, 'info@shopeaze.co.ke'])
    # fixme email template with this message
    remove_cart(request, user, order_string)


def remove_cart(request, user, order_string):
    # get order id
    order = Orders.objects.get(order_string=order_string)
    # create order items

    cart_items = Cart.objects.filter(user=user)
    # transfer cart items to order
    for item in cart_items:
        new_order_item = OrderItems.objects.create(order=order, quantity=item.qty, item=item.item)

    # delete cart
    cart_items.delete()


@login_required(login_url='customer-accounts:login')
def mpesa_loading(request):
    return render(request, 'shopeaze/payments/mpesa-waiting.html')


@login_required(login_url='customer-accounts:login')
def mobile_pesa_done(request):
    user = User.objects.get(pk=request.user.pk)
    print('{} is the merchant id'.format(request.session.get('mpesa_request_id')))
    payment = MpesaPayment.objects.filter(merchant_request_id=request.session.get('mpesa_request_id'))
    if payment.count() > 0:
        payment.update(customer=user, confirmation_status=True)
        orderString = [x.order_id for x in payment][0]
        # create order
        create_order(request=request, mode='Mpesa')
        return render(request, 'shopeaze/payments/order-done.html')

    else:
        return redirect('shop:mpesa_loading')
