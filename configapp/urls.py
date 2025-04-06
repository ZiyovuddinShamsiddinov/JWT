from os.path import basename
from django.contrib import admin
from django.urls import path, include
from configapp.routers import router
from configapp.models import CommitMovie
from configapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", MovieApi , basename="movie_api")
router.register(r"", ActorApi , basename="actor_api")

urlpatterns = [
    path("movie/", MovieApi.as_view(), name="movie-create"),  # Регистрируем вручную
    path("commit/",CommentApiI.as_view()),
    path('commit_details/<slug:slug>/', ),
    path("actor/",ActorApi.as_view()),
    path('actor_detail/<slug:slug>/', ),
    path('movie_detail/<slug:slug>/', ),


]

