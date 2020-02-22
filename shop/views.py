from django.shortcuts import render, redirect

# Create your views here.
from inventory.models import Inventory


def index(request):
    products = Inventory.objects.all().order_by('id')[:12]
    new_products = Inventory.objects.all().order_by('-time_added')[:12]
    return render(request, 'michpastries/index.html', {'products': products, 'new_products': new_products})


def wishlist(request):
    return render(request, 'michpastries/wishlist.html')


def product(request, pk):
    print(pk)
    product_details = Inventory.objects.get(pk=pk)
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
