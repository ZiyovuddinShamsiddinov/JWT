from os.path import basename
from django.contrib import admin
from django.urls import path, include
# from configapp.routers import router
from configapp.models import CommitMovie
from .views import *

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"", MovieCreateView , basename="movie_api")
# router.register(r"", MovieCreateView , basename="actor_api")

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='movie-list'),
    path('movie/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),

    path('actor/', MovieListView.as_view(), name='movie-list'),
    path('actor/create/', MovieCreateView.as_view(), name='movie-create'),
    path('actor/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('actor/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('actor/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),

    path('commit/', MovieListView.as_view(), name='movie-list'),
    path('commit/create/', MovieCreateView.as_view(), name='movie-create'),
    path('commit/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('commit/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('commit/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie-delete'),

]
