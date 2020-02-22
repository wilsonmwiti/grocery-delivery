from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from accounts.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'location', 'password1', 'password2')


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=254)

    class Meta:
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }


class NewPassword(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=20)
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20)

    class Meta:
        fields = ('password1', 'password2')


class ContactUsForm(forms.Form):
    # phone.email,message,name
    phone = forms.CharField(max_length=20)
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 8, "cols": 30}))

    class Meta:
        fields = ('phone', 'name', 'email', 'message',)
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input100',
            'placeholder': '',
            'id': 'hi',
        }
    ))
