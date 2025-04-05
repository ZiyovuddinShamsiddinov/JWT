from django.contrib import admin
from django.urls import path, include
from tutorial.urls import router

from configapp.models import CommitMovie
from configapp.views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"", MovieApi)

urlpatterns = [
    path("movie/", MovieApi.as_view(), name="movie-create"),  # Регистрируем вручную
    path("commit/",CommentAPI.as_view()),

    # # path('malumot_api/', malumot_api),
    # path("movie/",MovieApi.as_view()),
    # # get,post
    # path('movie_api/', movie_api),
    # # put,patch,delete
    # path('movie_detail/<slug:slug>/', movie_details),

    # path("movie_details/<int:pk>",MovieDetailApi.as_view()),
]

