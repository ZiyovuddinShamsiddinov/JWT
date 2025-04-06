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
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action

class MovieApi(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(request):
        response = {"success": True}
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        response["data"] = serializer.data

        return Response(data=response)
    def post(self, request):
        response = {"success": True}
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['data'] = serializer.data
            return Response(data=response)
        return Response(data=serializer.data)

    # def delete(self,request):
    #
    # def put(self,request):
    #
    # def patch(self,request):

class ActorApi(CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request):
        response = {"success": True}
        commits = CommitMovie.objects.all()
        serializer = CommitSerializer(commits, many=True)
        response["data"] = serializer.data
        return Response(data=response)

    def post(self, request):
        response = {"success": True}
        serializer = CommitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['data'] = serializer.data
            return Response(data=response)
        return Response(data=serializer.data)

    # def delete(self,request):
    #
    # def put(self,request):
    #
    # def patch(self,request):

class CommentApi(CreateAPIView):
    queryset = CommitMovie.objects.all()
    serializer_class = CommitSerializer

    def get(self, request):
        response = {"success": True}
        commits = CommitMovie.objects.all()
        serializer = CommitSerializer(commits, many=True)
        response["data"] = serializer.data
        return Response(data=response)

    def post(self, request):
        response = {"success": True}
        serializer = CommitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['data'] = serializer.data
            return Response(data=response)
        return Response(data=serializer.data)

    # def delete(self,request):
    #
    # def put(self,request):
    #
    # def patch(self,request):


# class MovieDetailApi(CreateAPIView):
#
#     def get(self, request, pk):
#         response = {"succes": True}
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             response["data"] = serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response)
#
#     def put(self, request, pk):
#         response = {"succes": True}
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response)
#
#     def patch(self, request, pk):
#         response = {"succes": True}
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response)


# class ActorApi(CreateAPIView):
#
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         data = {"succes": True}
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             data["serializer"] = serializer.data
#             return Response(data=data)
#         data["succes"] = False
#         return Response(data=data)

# class ActorDetailsApi(CreateAPIView):


# class CommentDetailApi(CreateAPIView):
#
#     def get(self, request, pk):
#         response = {"succes": True}
#         try:
#             commit = CommitMovie.objects.get(pk=pk)
#             serializer = CommitSerializer(commit)
#             response["data"] = serializer.data
#             return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response)
#
#     def put(self, request, pk):
#         response = {"succes": True}
#         try:
#             commit = CommitMovie.objects.get(pk=pk)
#             serializer = CommitSerializer(commit)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response)
#
#     def patch(self, request, pk):
#         response = {"succes": True}
#         try:
#             commit = CommitMovie.objects.get(pk=pk)
#             serializer = CommitSerializer(commit)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 response["data"] = serializer.data
#                 return Response(data=response)
#         except Movie.DoesNotExist:
#             response['succes'] = False
#             return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
