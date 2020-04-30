from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from django import forms

from inventory.models import Inventory
from shop.models import Orders


class InventoryAdditionForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['item_name', 'price_per_unit', 'image', 'category', 'discount', 'discounted', 'owner']
        widgets = {'owner': forms.HiddenInput(), 'image': forms.FileInput(attrs={'class': 'form-control-file'})}

    def __init__(self, *args, **kwargs):
        super(InventoryAdditionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            'imagefile',
            HTML(
                """{% if form.imagefile.value %}<img class="img-responsive" src="{{ MEDIA_URL }}
                {{ form.imagefile.value }}">{% endif %}""", ),

        )


class CashAcceptanceForm(forms.ModelForm):
    paid = forms.BooleanField(label="Confirm cash reception")

    class Meta:
        model = Orders
        fields = ['store', 'order_string', 'payment_mode', 'amount', 'paid']
        widgets = {'store': forms.HiddenInput(),
                   'order_string': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'payment_mode': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'amount': forms.TextInput(attrs={'readonly': 'readonly'}),

                   }
