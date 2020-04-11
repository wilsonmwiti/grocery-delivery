from django.shortcuts import render

from accounts.models import User
from sellers.forms import InventoryAdditionForm
from sellers.models import StoreLine, Stores


def panel(request):
    user = User.objects.get(pk=request.user.pk)
    stores = Stores.objects.get(admin=user)
    # todo start with logo and brand display tomorrow after creating calling service document for amanda
    line = StoreLine.objects.filter(pk=stores.line.pk)
    line = StoreLine.objects.filter(pk=stores.line.pk)

    if line.count() > 0:
        stores = Stores.objects.filter(line__admin=user)
        inventory_form = InventoryAdditionForm()
        return render(request, 'shopeaze/staff-panel/panel-home.html',
                      {'line': line, 'stores': stores, 'StoresForm': inventory_form})


def additems(request):
    return None


def sales(request):
    return None


def orders(request):
    return None


def reports(request):
    return None


def messages(request):
    return None
