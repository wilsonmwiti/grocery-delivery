import json

import requests
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from requests.auth import HTTPBasicAuth

from accounts.models import User
from mpesa_api.models import MpesaPayment
from mpesa_api.mpesa_credentials import MpesaAccessToken, LipanaMpesaPassword, MpesaC2bCredential
from shop.models import Cart


def getAccessToken(request):
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


# for stk push
def lipa_na_mpesa_online(request):

    user = User.objects.get(pk=request.user.pk)
    phone_number = '254' + user.profile.mobile_money_phone_number[-9:]
    cart = Cart.objects.filter(user=user)
    cart_total = 0
    for item in cart:
        cart_total += item.price

    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request_post = {
        "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
        "Password": LipanaMpesaPassword.decode_password,
        "Timestamp": LipanaMpesaPassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",  # CustomerBuyGoodsOnline #for till number
        "Amount": cart_total,
        "PartyA": phone_number,
        "PartyB": LipanaMpesaPassword.Business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://d81ab4d1.ngrok.io/mobile-pesa-api/v1/c2b/confirmation",
        "AccountReference": "Shop Eaze",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request_post, headers=headers)
    dict = json.loads(response.text)
    # next(item for item in item_dicts if item["Name"] == "Amount")['Value']
    request.session['mpesa_request_id'] = dict['MerchantRequestID']
    return redirect('shop:mpesa_loading')


@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               # todo remember to fix ngrok link
               "ConfirmationURL": "https://d81ab4d1.ngrok.io/mobile-pesa-api/v1/c2b/confirmation",
               "ValidationURL": "https://d81ab4d1.ngrok.io/mobile-pesa-api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def call_back(request):
    pass


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    print(request.user.pk)

    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    transaction_dict = mpesa_payment['Body']['stkCallback']
    item_dicts = mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item']

    payment = MpesaPayment.objects.create(
        amount=next(item for item in item_dicts if item["Name"] == "Amount")['Value'],
        reference=
        next(item for item in item_dicts if item["Name"] == "MpesaReceiptNumber")[
            'Value'],
        merchant_request_id=transaction_dict['MerchantRequestID'],
        CheckoutRequestID=transaction_dict['CheckoutRequestID'],
        ResultDesc=transaction_dict['ResultDesc'], phone_number=
        next(item for item in item_dicts if item["Name"] == "PhoneNumber")['Value'],
        organization_balance='')
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
