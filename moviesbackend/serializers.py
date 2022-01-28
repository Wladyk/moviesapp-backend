from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email", "watchLaterList"]
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    class Meta:
        model = Movie
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    movie = MovieSerializer()
    class Meta:
        model = Rating
        fields = "__all__"

class WatchLaterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    movie = MovieSerializer()
    class Meta:
        model = WatchLater
        fields = "__all__"