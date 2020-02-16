from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'michpastries/index.html')


def wishlist(request):
    return render(request, 'michpastries/wishlist.html')


def product(request):
    return render(request, 'michpastries/product-single.html')


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
