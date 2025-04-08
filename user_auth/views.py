from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .make_token import *
from .serializer import *
from functools import partial
from http.client import responses
from turtledemo.clock import datum
from django.core.serializers import serialize
from django.shortcuts import render
from django.template.defaulttags import comment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.decorators import action

class LoginApi(APIView):
    permission_classes = [AllowAny,]

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data.get("user")
        token=get_tokens_for_user(user)
        token["salom"]="hi"
        token["is_admin"]=user.is_superuser

        return Response(data=token,status=status.HTTP_200_OK)