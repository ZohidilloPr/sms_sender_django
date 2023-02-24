from .models import Phone, CustomUser
from rest_framework import serializers


class GETPhone(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone"]
