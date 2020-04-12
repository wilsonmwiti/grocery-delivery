from django.shortcuts import render, redirect

from accounts.models import User
from inventory.models import Inventory
from sellers.models import StoreLine, Stores
from shop.forms import SearchForm
from staffapp.forms import InventoryAdditionForm


def panel(request):
    user = User.objects.get(pk=request.user.pk)
    stores = Stores.objects.get(admin=user)
    search_form = SearchForm()

    # todo start with logo and brand display tomorrow after creating calling service document for amanda
    line = StoreLine.objects.get(pk=stores.line.pk)
    if line:
        store = Stores.objects.get(admin=user)
        items = Inventory.objects.filter(owner=store)
        inventory_form = InventoryAdditionForm()
        return render(request, 'shopeaze/staff-panel/panel-home.html',
                      {'line': line, 'store': store, 'InventoryForm': inventory_form, 'search_form': search_form,
                       'items': items})


def additems(request):
    user = User.objects.get(pk=request.user.pk)
    store = Stores.objects.get(admin=user)
    if request.method == 'POST':
        form = InventoryAdditionForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = store
            obj.save()
            return redirect('staff:panel')
        else:
            print(form.errors)
            print('invalid form')


def sales(request):
    return None


def orders(request):
    return None


def reports(request):
    return None


def messages(request):
    return None


def updateitem(request, hash):
    user = User.objects.get(pk=request.user.pk)
    stores = Stores.objects.get(admin=user)
    search_form = SearchForm()

    # todo start with logo and brand display tomorrow after creating calling service document for amanda
    line = StoreLine.objects.get(pk=stores.line.pk)
    item = Inventory.objects.get(hash=hash)
    form = InventoryAdditionForm(initial={'item_name': item.item_name, 'image': item.image, 'category': item.category,
                                          'price_per_unit': item.price_per_unit, 'discount': item.discount,
                                          'discounted': item.discounted})
    if request.method == 'POST':
        form = InventoryAdditionForm(request.POST, request.FILES, instance=item)
        store = Stores.objects.get(admin=user)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = store
            obj.save()
        else:
            print(form.errors)
    return render(request, 'shopeaze/staff-panel/bounded_form.html',
                  {'line': line, 'form': form, 'search_form': search_form, 'item': item
                   })
