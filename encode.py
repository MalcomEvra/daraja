import consts
import base64


def generate_password(formatted_time):
    #Generating Password (Shortcode,passkey and Timestamp)
    data_to_encode=consts.business_shortCode + consts.lipa_na_mpesa_passkey + formatted_time
    encoded_string =base64.b64encode(data_to_encode.encode())

    decode_password=encoded_string.decode('utf-8')
    #print(decode_password)
    return decode_password