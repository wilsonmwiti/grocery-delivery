from django import forms


# class QuantityForm(forms.Form):
#     qty = forms.IntegerField()
#
#     class Meta:
#         widgets = {
#             'qty': forms.TextInput(attrs={'class': 'myfieldclass', 'step': '1'}),
#         }


class QuantityForm(forms.Form):
    qty = forms.IntegerField()
    size = forms.IntegerField()

    class Meta:
        widgets = {
            'qty': forms.TextInput(attrs={'class': 'myfieldclass', 'step': '1'}),
            'size': forms.TextInput(attrs={'class': 'myfieldclass', 'step': '0.5'}),
        }
