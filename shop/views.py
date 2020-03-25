from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from accounts.models import User
from inventory.models import Inventory, Categories
from shop.forms import QuantityForm, QuantityFormCuppy
from shop.models import Cart, WishList


def index(request):
    products = Inventory.objects.all().order_by('id')[:12]
    cart_items = Cart.objects.all().count()
    new_products = Inventory.objects.all().order_by('-time_added')[:4]
    return render(request, 'michpastries/index.html',
                  {'products': products, 'new_products': new_products, 'cart_count': cart_items})


@login_required(login_url='customer-accounts:login')
def add_wish(request, pk):
    print("in wishes")
    user = User.objects.get(pk=request.user.pk)
    wishobj = WishList.objects.filter(user=user)
    item = Inventory.objects.get(pk=pk)
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
def delete_wish(request, pk):
    user = User.objects.get(pk=request.user.pk)
    item = Inventory.objects.get(pk=pk)
    remove_item = WishList.objects.filter(user=user, item=item)
    remove_item.delete()
    return redirect("shop:wishlist")


@login_required(login_url='customer-accounts:login')
def wishlist(request):
    wishes = WishList.objects.filter(user=request.user.pk)

    return render(request, 'michpastries/wishlist.html', {'wishes': wishes})


def product(request, pk):
    # print(pk)
    form = QuantityForm()
    product_details = get_object_or_404(Inventory, pk=pk)
    return render(request, 'michpastries/product-single.html', {'product': product_details, 'form': form})


# 198919
@login_required(login_url='customer-accounts:login')
def cart(request):
    # user=User.objects.filter(pk=request.user.pk)
    cart = Cart.objects.filter(user=request.user.pk)
    cart_total = 0
    for x in cart:
        cart_total += x.price
    return render(request, 'michpastries/cart.html', {'cart': cart, 'sum': cart_total})


@login_required(login_url='customer-accounts:login')
def checkout(request):
    return render(request, 'michpastries/checkout.html')


def about(request):
    return render(request, 'michpastries/about.html')


def contact(request):
    return render(request, 'michpastries/contact.html')


def login(request):
    return redirect('customer-accounts:login')


# @login_required(login_url='customer-accounts:login')
# def add_to_cart(request, pk):
#     print("add to cart")
#     if request.method == 'POST':
#         print("post")
#         if request.user.is_authenticated:
#             form = QuantityForm(request.POST)
#             print(form.errors)
#             if form.is_valid():
#
#                 qty = form.cleaned_data.get("quantity")
#                 size = form.cleaned_data.get("size")
#                 user = request.user.pk
#                 cartobj = Cart.objects.filter(user=user)
#                 item = Inventory.objects.get(pk=pk)
#                 if cartobj:
#                     # users cart exists
#                     obj = Cart.objects.filter(user=user, item=item)
#                     if obj:
#                         #     object exists in cart
#                         obj.update(qty=qty, size=size)
#                     else:
#                         # object does not exist in cart
#                         cartobj = Cart.objects.create(user=user, qty=qty, item=item, size=size)
#
#                 else:
#                     # user cart does not exist
#                     cartobj = Cart.objects.create(user=user, qty=qty, item=item, size=size)
#             else:
#                 print("invalid form")
#     else:
#         return render(request, 'michpastries/accounts/login.html')
#     next = request.POST.get('next', '/')
#     print("redirection")
#     return HttpResponseRedirect(next)


def categories(request, pk):
    products = Inventory.objects.filter(category=pk)
    cat = get_object_or_404(Categories, pk=pk)

    cart_items = Cart.objects.filter(user=request.user.pk).count()
    return render(request, 'michpastries/categories.html',
                  {'products': products, 'cart_count': cart_items, 'category': cat, })


@login_required(login_url='customer-accounts:login')
def remove_from_cart(request, pk):
    # removing from cart
    print(pk)
    user = User.objects.get(pk=request.user.pk)
    item = Inventory.objects.get(pk=pk)
    remove_item = Cart.objects.filter(user=user, item=item)
    remove_item.delete()
    return redirect('shop:cart')


@login_required(login_url='customer-accounts:login')
def cuppy_add(request, pk):
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
                    obj = Cart.objects.filter(user=user, item=item)
                    if obj:
                        #     if object exists in cart
                        obj.update(qty=qty)
                        # obj.save()
                    else:
                        # object does not exist in cart
                        cartobj = Cart.objects.create(user=user, qty=qty, item=item)

                else:
                    # user cart does not exist
                    cartobj = Cart.objects.create(user=user, qty=qty, item=item)
            else:
                print("invalid form")
    else:
        return render(request, 'michpastries/accounts/login.html')
    next = request.POST.get('next', '/')
    print("redirection")
    return HttpResponseRedirect(next)


def single_add(request, pk):
    user = User.objects.get(pk=request.user.pk)
    cartobj = Cart.objects.filter(user=user)
    item = Inventory.objects.get(pk=pk)
    if cartobj:
        # if users cart exists
        obj = Cart.objects.filter(user=user, item=item)
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
