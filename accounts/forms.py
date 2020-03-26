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
    sender_name = forms.CharField(required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    sender_mail = forms.EmailField(required=True,
                                   widget=forms.EmailInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    mail_subject = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Your Subject'}))

    mail_message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message here....', "rows": 7, "cols": 30}))


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
