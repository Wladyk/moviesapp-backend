from rest_framework import viewsets
from moviesbackend.models import *
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

class GenreViewset(viewsets.ModelViewSet):
    serializer_class = serializers.GenreSerializer
    queryset = Genre.objects.all()

class MovieViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MovieSerializer
    queryset = Movie.objects.all()

class RatingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RatingSerializer
    queryset = Rating.objects.all()

class WatchLaterViewset(viewsets.ModelViewSet):
    serializer_class = serializers.WatchLaterSerializer
    queryset = WatchLater.objects.all()