import os
import random
from .models import CustomUser
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .serializers import GETPhone, UserSerializer
from rest_framework.views import APIView, Response
from infobip_api_client.exceptions import ApiException
from infobip_api_client.api.send_sms_api import SendSmsApi
from infobip_api_client.model.sms_response import SmsResponse
from infobip_api_client.api_client import ApiClient, Configuration
from infobip_api_client.model.sms_destination import SmsDestination
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from infobip_api_client.model.sms_textual_message import SmsTextualMessage
from infobip_api_client.model.sms_advanced_textual_request import SmsAdvancedTextualRequest

# Create your views here.

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


def Validate_Phone(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            phone = request.POST.get("phone")
            RECIPIENT = f"998{phone}"
            user = CustomUser.objects.get(id=request.user.id)
            user.phone=phone
            password = int(random.randint(111, 999))
            user.validate_code = password
            print(password)
            MESSAGE_TEXT = f"Sizning parolingiz {password}, buni hech kimga bermang."
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
            except ApiException as ex:
                print("Error occurred while trying to send SMS message.")
                print(ex)
            user.save()
            return redirect("conf")
    return render(request, "index.htm")



def VerifyCode(request):
    # print(f"VALIDATE CODE FOR {request.user.username}", request.user.validate_code)
    if request.method == "POST":
        validate_code = int(request.POST.get("validate_code"))
        if request.user.validate_code == validate_code:
            user = CustomUser.objects.get(id=request.user.id)
            user.validate=True
            user.save()
            print("VALIDATED USER IS SUCCESSFULLY")
        else:
            print("VALIDATED USER IS NOT SUCCESSFULLY")
    return render(request, "conf.htm")

    
class GETPhoneView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        password = int(random.randint(111, 999))
        MESSAGE_TEXT = f"Sizning parolingiz {password}, buni hech kimga bermang."
        print(MESSAGE_TEXT)
        return serializer.save(validate_code=password)

    
    

