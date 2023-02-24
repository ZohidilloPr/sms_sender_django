import os
import random
from .forms import ConfForm
from dotenv import load_dotenv
from .models import ConfirmPassword
from django.shortcuts import render, redirect
from infobip_api_client.exceptions import ApiException
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_destination import SmsDestination
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest

""" START API SETTINGS """

load_dotenv('.env')  
BASE_URL = os.getenv('INFOBIP_BASE_URL')
API_KEY = os.getenv('INFOBIP_API_KEY')

SENDER = "ZohidilloPr"
RECIPIENT = ""
password = random.randint(111111, 999999)
MESSAGE_TEXT = f"Sizning parolingiz {password}, buni hech kimga bermang."


client_config = Configuration(
    host=BASE_URL,
    api_key={"APIKeyHeader": API_KEY},
    api_key_prefix={"APIKeyHeader": "App"},
)
api_client = ApiClient(client_config)

""" END API SETTINGS """

def Home(request):
    if request.method == "POST":
        form = ConfForm(request.POST)
        phone = request.POST.get("tel")
        RECIPIENT = f"998{phone}"
        conf_p = ConfirmPassword.objects.create(phone=phone, sms_code=password)
        conf_p.save()
        sms_request = SmsAdvancedTextualRequest(
            messages=[
                SmsTextualMessage(
                    destinations=[
                        SmsDestination(
                            to=RECIPIENT,
                        ),
                    ],
                    _from=SENDER,
                    text=MESSAGE_TEXT,
                )
            ]
        )
        api_instance = SendSmsApi(api_client)
        try:
            api_response: SmsResponse = api_instance.send_sms_message(sms_advanced_textual_request=sms_request)
            # print(api_response)
            return redirect("conf")
        except ApiException as ex:
            print("Error occurred while trying to send SMS message.")
            print(ex)
    return render(request, "index.htm")

def ConfirmPassword(request):
    if request.method == "POST":
        con_password = request.POST.get("confirm_password")
        if password == con_password:
            print(password, "It is OK")
        else:
            print("Something is went wrong :(")
    return render(request, "conf.htm")
