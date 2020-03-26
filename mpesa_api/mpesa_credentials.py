import base64
import json
from datetime import datetime

import requests
from requests.auth import HTTPBasicAuth


class MpesaC2bCredential:
    consumer_key = 'AAbaduj3bwwTCBuyAZNonGsyLdUHpvfS'  # my consumer key
    consumer_secret = 'AMVGtMd3V3bqAZc9'  # my consumer secret
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    # use in testing environment
    # Business_short_code = "174379"  # 525522
    # Test_c2b_shortcode = "600344"  # todo change to businesses till number
    # use in production environment
    Business_short_code = "525522"  # 525522 is till number
    Test_c2b_shortcode = "525522"  # todo change to businesses till number
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
