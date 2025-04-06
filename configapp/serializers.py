from rest_framework import serializers
from .models import *


# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Movie
#         fields="__all__"

class ActorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    birth_date = serializers.DateField()

    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    slug = serializers.SlugField(read_only=True)
    year = serializers.IntegerField()
    actor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    genre = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    class Meta:
        model = Movie
        fields = "__all__"


class CommitSerializer(serializers.ModelSerializer):
    # author=serializers.(read_only=True)
    class Meta:
        model = CommitMovie
        fields = ["id","title","author","movie"]
