from msilib.schema import Registry

from django.urls import path
from .views import *

urlpatterns = [
    path('auth/login/', LoginApi.as_view(), name='login'),
    path('post_phone_send_otp/', PhoneSendOTP.as_view()),
    path('post_phone_v_otp/', PhoneSendOTP.as_view()),
    path('register/', RegistrUserApi.as_view()),

]
