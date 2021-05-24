from django import forms


# class QuantityForm(forms.Form):
#     qty = forms.IntegerField()
#
#     class Meta:
#         widgets = {
#             'qty': forms.TextInput(attrs={'class': 'myfieldclass', 'step': '1'}),
#         }


class QuantityForm(forms.Form):
    qty = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control input-number", 'id': 'quantity',
        'value': "1", 'min': "1", 'step': "1"}))
    # next = forms.CharField()
    # size = forms.IntegerField(widget=forms.TextInput(attrs={
    #     'class': "form-control input-number", 'id': 'size',
    #     'min': "0.5", 'step': "0.5", 'max': '20'}),initial=0.5)


class QuantityFormCuppy(forms.Form):
    qty = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': "form-control input-number", 'id': 'quantity',
        'value': "4", 'min': "4", 'step': "1"}), required=False)


class SubscribeForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))


class SearchForm(forms.Form):
    item = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={'class': "form-control form-control-sm  w-50 mr-2 rounded mb-2 p-2",
                                      'placeholder': 'item name'}),
                           label='')

class SearchOrderForm(forms.Form):
    order_id = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'class': "form-control form-control-sm  w-50 mr-2 rounded mb-2 p-2",
                                          'placeholder': 'Input Order Id'}),
                               label='')


class SearchStoresForm(forms.Form):
    store = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'class': "form-control form-control-sm  w-50 mr-2 rounded mb-2 p-2",
                                       'placeholder': 'Town/City...'}),
                            label='')


class PaymentsForm(forms.Form):
    payment = [
        ('mpesastk', 'Mpesa Express'),
        ('cash', 'Cash on delivery'),
    ]
    payment_choices = forms.ChoiceField(label='', choices=payment, widget=forms.RadioSelect(attrs={'class': "mr-2"}))
