from django import forms

from sellers.models import Stores


class StoresLineCreationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store  Line  Name'}))
    logo = forms.ImageField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'col-md-6 mb-0', 'placeholder': 'What you deal with'}))


class StoresCreationForm(forms.ModelForm):
    class Meta:
        model = Stores
        fields = ['town', 'name', 'phone_number', 'email']
        widgets = {
            'town': forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Town/City'}),
            'name': forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Name(Optional'}),
            'phone_number': forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Phone Number'}),
            'email': forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Email'}),
        }
    # town = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Town/City'}))
    # name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Name(Optional)'}))
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Phone Number'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Email'}))
