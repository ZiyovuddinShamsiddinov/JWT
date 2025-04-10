from functools import cache
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import password_changed
from django.db.models.fields import return_None
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from tutorial.quickstart.serializers import UserSerializer

from ..models import *
from ..serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
import random


class LoginApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = get_tokens_for_user(user)
        token["is_admin"] = user.is_admin
        return Response(token, status=status.HTTP_200_OK)


class PhoneSendOTP(APIView):
    @swagger_auto_schema(request_body=SMSSerializer)
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')

        if phone_number:
            phone = str(phone_number)
            user = User.objects.filter(phone_number__iexact=phone)
            if user.exists():
                return Response({
                    'status': False,
                    'details': 'phone numberalredy exists'
                })
            else:
                key = send_otp()
                if key:
                    cache.set(phone_number, key, 600)

                    return Response({"massage": "SMS send successfully"}, status=status.HTTP_200_OK)

                return Response({"massage": "Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)


def send_otp():
    otp = str(random.randint(1001, 9999))
    return otp

class VerifySMS(APIView):
    @swagger_auto_schema(request_body=VerifySMSSerializer)
    def post(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']
            cached_code = str(cache.get(phone_number))
            if verification_code == str(cached_code):
                return Response({
                    'status': True,
                    'detail': 'OTP matched. please proceed for registration'
                })
            else:
                return Response({
                    'status': False,
                    'detail': 'OTP INCORRECT'
                })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserApi(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,requset):
        serializer=UserSerializer(data=requset.data)
        if serializer.is_valid(raise_exception=True):
            password=serializer.validated_data.get('password')
            serializer.validated_data['password']=make_password(password)
            serializer.save()
            return Response({
                'status':True,
                'details':'Account create'
            })

    def get(self,request):
        users=User.objects.all().order_by('-id')
        serializer=UserSerializer(users,many=True)
        return Response(data=serializer.data)