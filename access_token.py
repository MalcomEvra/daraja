import requests
import consts
from requests.auth import HTTPBasicAuth

def generate_access_token():

    #AccesToken  Generation
    consumer_key = consts.consumer_key
    consumer_secret = consts.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    
    print (r.json())
    json_response=r.json()
    my_access_token=json_response['access_token'] 
    return my_access_token