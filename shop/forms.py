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
    qty = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control input-number", 'id': 'quantity',
        'value': "4", 'min': "4", 'step': "1"}), required=False)