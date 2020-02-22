from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from inventory.models import Inventory
from shop.models import Cart


def index(request):
    products = Inventory.objects.all().order_by('id')[:12]

    new_products = Inventory.objects.all().order_by('-time_added')[:12]
    return render(request, 'michpastries/index.html', {'products': products, 'new_products': new_products})


def wishlist(request):
    return render(request, 'michpastries/wishlist.html')


def product(request, pk):
    print(pk)
    product_details = get_object_or_404(Inventory, pk=pk)
    return render(request, 'michpastries/product-single.html', {'product': product_details})


def cart(request):
    return render(request, 'michpastries/cart.html')


def checkout(request):
    return render(request, 'michpastries/checkout.html')


def about(request):
    return render(request, 'michpastries/about.html')


def contact(request):
    return render(request, 'michpastries/contact.html')


def login(request):
    return redirect('accounts:login')


def add_to_cart(request, pk):
    qty = 0
    # todo proceed here next by creating a cart functionality
    product_details = get_object_or_404(Inventory, pk=pk)
    cart = Cart.objects.get(user=request.user.pk, item=pk)
    if cart:
        cart.qty = cart.qty + qty
        cart.save()
    else:
        cart = Cart.objects.create(user=request.user.pk, item=pk, qty=qty)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
