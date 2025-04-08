from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "details":"User does not exist"
                }
            )
        auth_user=authenticate(username=user.username,password=password)
        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "success":False,
                    "detail":"Username or password is invalid"
                }
            )
        attrs["user"]=auth_user
        return attrs