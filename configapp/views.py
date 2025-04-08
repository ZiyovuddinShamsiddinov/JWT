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


# CREATE
class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# READ ALL
class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# READ ONE
class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# UPDATE
class MovieUpdateView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# DELETE
class MovieDeleteView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# CREATE
class ActorCreateView(CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# READ ALL
class ActorListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# READ ONE
class ActorDetailView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# UPDATE
class ActorUpdateView(UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# DELETE
class ActorDeleteView(DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

# CREATE
class CommitCreateView(CreateAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer
# READ ALL
class CommitListView(ListAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer
# READ ONE
class CommitDetailView(RetrieveAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer
# UPDATE
class CommitUpdateView(UpdateAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer
# DELETE
class CommitDeleteView(DestroyAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer



