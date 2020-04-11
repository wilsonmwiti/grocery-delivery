from django import forms

from inventory.models import Inventory


class InventoryAdditionForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'price_per_unit', 'image', 'category', 'discount', 'discounted', 'owner']
        widgets = {'owner': forms.HiddenInput()}
