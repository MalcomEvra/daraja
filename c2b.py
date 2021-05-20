import requests
import consts
from access_token import generate_access_token


def register_url():
  my_access_token=generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
  headers = {"Authorization": "Bearer %s" % my_access_token}
  request = { "ShortCode": consts.shortcode,
      "ResponseType": "Complete ",
      "ConfirmationURL": "http://chalevsolutions.com/confirmation_url",
      "ValidationURL": "http://chalevsolutions.com/validation_url"
      }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
#register_url()
def simulate_c2b_transaction():
  
  access_token = generate_access_token()
  api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
  headers = {"Authorization": "Bearer %s" % access_token}
  request = { 
    "ShortCode":consts.shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"2",
    "Msisdn":consts.test_msisdn,
    "BillRefNumber":"2845745 "
     }
  
  response = requests.post(api_url, json = request, headers=headers)
  
  print (response.text)
simulate_c2b_transaction()

