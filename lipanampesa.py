import requests
import consts
from utils import get_timestamp
from encode import generate_password
from access_token import generate_access_token



def lipa_na_mpesa():
        formatted_time=get_timestamp()
        decode_password= generate_password(formatted_time)

        access_token = generate_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = { "Authorization": "Bearer %s" % access_token }
        request = {
            "BusinessShortCode": consts.business_shortCode,
            "Password": decode_password,
            "Timestamp": formatted_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "5",
            "PartyA": consts.phone_number,
            "PartyB": consts.business_shortCode,
            "PhoneNumber": consts.phone_number,
            "CallBackURL": "https://chalevsolutions.com/lipanampesa/",
            "AccountReference": "Chalev Solutions",
            "TransactionDesc": "School fees "
        }
        
        response = requests.post(api_url, json = request, headers=headers)
        
        print (response.text)
lipa_na_mpesa()

