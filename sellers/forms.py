from django import forms


class StoresLineCreationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store  Line  Name'}))
    logo = forms.ImageField()
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'col-md-6 mb-0', 'placeholder': 'What you deal with'}))


class StoresCreationForm(forms.Form):
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Town/City'}))
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Phone Number'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'col-md-6 mb-0', 'placeholder': 'Store Email'}))


