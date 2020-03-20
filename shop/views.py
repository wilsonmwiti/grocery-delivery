from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from inventory.models import Inventory, Categories
from shop.models import Cart


def index(request):
    products = Inventory.objects.all().order_by('id')[:12]
    cart_items = Cart.objects.all().count()
    new_products = Inventory.objects.all().order_by('-time_added')[:4]
    return render(request, 'michpastries/index.html',
                  {'products': products, 'new_products': new_products, 'cart_count': cart_items})


@login_required(login_url='customer-accounts:login')
def wishlist(request):
    return render(request, 'michpastries/wishlist.html')


def product(request, pk):
    print(pk)
    product_details = get_object_or_404(Inventory, pk=pk)
    return render(request, 'michpastries/product-single.html', {'product': product_details})


# 198919
@login_required(login_url='customer-accounts:login')
def cart(request):
    if request.user.is_authenticated:
        cartobj = Cart.objects.get(user=request.user.pk)
        if request.method == 'POST':
            print("add to cart loaded")
            if request.user.is_authenticated:
                qty = 0
                # todo proceed from here next time by creating a cart functionality
                # product_details = get_object_or_404(Inventory, pk=pk)
                cart = Cart.objects.get(user=request.user.pk)
                if cart:
                    cart.qty = cart.qty + qty
                    cart.save()
                else:
                    cart = Cart.objects.create(user=request.user.pk, qty=qty)

        else:

            return render(request, 'michpastries/cart.html', {'cart': cartobj})
    else:
        return render(request, 'michpastries/accounts/login.html')


@login_required(login_url='customer-accounts:login')
def checkout(request):
    return render(request, 'michpastries/checkout.html')


def about(request):
    return render(request, 'michpastries/about.html')


def contact(request):
    return render(request, 'michpastries/contact.html')


def login(request):
    return redirect('customer-accounts:login')


@login_required(login_url='customer-accounts:login')
def add_to_cart(request, pk):
    # next = request.POST.get('next', '/')
    # return HttpResponseRedirect(next)
    #
    # return redirect('customer-accounts:login')
    pass


def categories(request, pk):
    products = Inventory.objects.filter(category=pk)
    cat = get_object_or_404(Categories, pk=pk)

    cart_items = Cart.objects.filter(user=request.user.pk).count()
    return render(request, 'michpastries/categories.html',
                  {'products': products, 'cart_count': cart_items, 'category': cat, })
