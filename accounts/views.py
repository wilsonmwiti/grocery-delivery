from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import SignUpForm, ForgotPasswordForm
from accounts.models import User
from .tokens import account_activation_token


@login_required(login_url='customer-accounts:login')
def panel(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % ('customer-accounts:login', request.path))
    user = User.objects.get(pk=request.user.pk)
    if user.user_type == "customer":
        if user.email_confirmed:
            return redirect('shop:index')
        else:
            return HttpResponse("<p>Please verify your account using the link sent to your email address</p>")

    elif user.user_type == "staff":
        return HttpResponse("<p>Staff panel</p>")
    elif user.user_type == 'seller':
        return redirect('sellers:panel')
    elif user.user_type == "admin":
        return HttpResponse("<p> Admin panel</p>")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('shopeaze/customer-accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(
                subject,
                message,
                'info@nanotechsoftwares.co.ke',
                [user.__str__()],
                fail_silently=False,
            )

            return redirect('customer-accounts:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'shopeaze/customer-accounts/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'shopeaze/customer-accounts/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True

        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('customer-accounts:panel')
    else:
        return render(request, 'shopeaze/customer-accounts/account_activation_invalid.html')


def resettoken(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True

        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('customer-accounts:panel')
    else:
        return render(request, 'shopeaze/customer-accounts/account_activation_invalid.html')


@login_required(login_url='customer-accounts:login')
def logout_view(request):
    logout(request)
    return redirect('shop:index')


def edit_profile(request):
    return None


def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data.get("email"))
                password = User.objects.make_random_password(length=8)
                user.set_password(password)
                user.save()
                current_site = get_current_site(request)
                subject = 'This is your new password'
                message = render_to_string('shopeaze/customer-accounts/password_reset.html', {
                    'user': user,
                    # 'domain': current_site.domain,
                    # 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    # 'token': account_activation_token.make_token(user),
                    'password': password,
                })
                send_mail(
                    subject,
                    message,
                    'info@nanotechsoftwares.co.ke',
                    [user.__str__()],
                    fail_silently=False,
                )
                print("sent email")
                return render(request, 'shopeaze/customer-accounts/reset-email-sent.html')
            except:
                print("user does not exist")
                messages.error(request, 'such an account does not exist')
                return redirect("customer-accounts:forgot")


        else:
            print("did not send email due to invalid form")
            form = ForgotPasswordForm()
            return render(request, 'shopeaze/customer-accounts/forgot.html', {'form': form})

    else:
        print("did not send email..just loaded the page")
        form = ForgotPasswordForm()
        return render(request, 'shopeaze/customer-accounts/forgot.html', {'form': form})


# def reset_password(request):
#     return None
# def reset_password(request, uidb64, token):
#     try:
#         print("resetting password")
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         request.session['userid'] = uidb64
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#
#     if user is not None and user.is_active and user.email_confirmed:
#         user.save()
#         print("redirect to db update stage")
#         return redirect('customer-accounts:enter_new_password')
#     else:
#         print('could not redirect to db update page')
#         form = ForgotPasswordForm()
#         return render(request, 'shopeaze/customer-accounts/forgot.html', {'form': form})


# def enter_new_password(request):
#     if request.method == 'POST':
#         form = EnterNewPassword(request.POST)
#         print("form error is{}".format(form.errors))
#         if form.is_valid():
#             password = form.cleaned_data.get('password1')
#             user = User.objects.get(pk=force_text(urlsafe_base64_decode(request.session.get("userid"))))
#             print(user.email)
#             user.password = password
#             user.save()
#             print("user password updated")
#             return redirect('customer-accounts:login')
#         else:
#             print("invalid form during password reset final phase")
#             return redirect('customer-accounts:enter_new_password')
#     else:
#         print("not post...just loaded up the file")
#         form = EnterNewPassword()
#
#         return render(request, 'shopeaze/customer-accounts/enter_new_password.html', {'form': form})
def profile(request):
    return redirect('customer-accounts:panel')
