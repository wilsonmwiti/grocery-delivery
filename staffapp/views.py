from django.shortcuts import render

from accounts.models import User
from sellers.forms import StoresLineCreationForm, StoresCreationForm
from sellers.models import StoreLine, Stores


def panel(request):
    user = User.objects.get(pk=request.user.pk)
    stores = Stores.objects.filter(admin=user)
    name = ''
    for x in stores:
        name = x.name
    # todo start with logo and brand display tomorrow after creating calling service document for amanda
    line = StoreLine.objects.filter(name=name)
    user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller')

    if line.count() > 0:
        user = User.objects.get(pk=request.user.pk)
        line = StoreLine.objects.filter(admin=user)
        stores = Stores.objects.filter(line__admin=user)
        user_is_seller = User.objects.filter(pk=request.user.pk, user_type='seller')
        store_line_form = StoresLineCreationForm()
        stores_form = StoresCreationForm()
        return render(request, 'shopeaze/staff-panel/panel-home.html',
                      {'line': line, 'stores': stores, 'StoreLineForm': store_line_form, 'StoresForm': stores_form,
                       'seller': user_is_seller})
