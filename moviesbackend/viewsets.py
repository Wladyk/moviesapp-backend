from rest_framework import viewsets, status
from moviesbackend.models import *
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
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

    def get_queryset(self):
        return Movie.objects.all().annotate(_averageRating=Avg('ratings__rating')) 
    def create(self, request):
        p_title = request.data.get('title')
        p_plot = request.data.get('plot') 
        p_averageRating = request.data.get('averageRating')
        p_releaseDate = request.data.get('releaseDate')
        p_genreId = request.data.get('genreId')
        p_genre = Genre.objects.filter(id=p_genreId).first()
        newMovie = Movie(title=p_title, plot=p_plot, averageRating=p_averageRating,
        releaseDate = p_releaseDate, genre=p_genre)
        newMovie.save()
        serialized = self.get_serializer(newMovie)
        return Response(serialized.data)


class RatingViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RatingSerializer
    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    # Standard request initializer has been overwritten to allow for different perms for each action
    def initialize_request(self, request, *args, **kwargs):
        self.action = self.action_map.get(request.method.lower())
        return super().initialize_request(request, *args, **kwargs)
    def get_authenticators(self):
        #The "list" action is unprotected, so any user can see ratings for a given movie
        if self.action == 'list':
            return []
        return super().get_authenticators()
    def create(self, request):
        p_rating = request.data.get('rating')
        userId = request.user.id
        p_author = User.objects.filter(id=userId).first()
        movieId = request.data.get('movieId')
        p_movie = Movie.objects.filter(id=movieId).first()
        p_message = request.data.get('message')
        newRating = Rating(rating = p_rating, author = p_author, movie = p_movie,
        message = p_message)
        newRating.save()
        serialized = self.get_serializer(newRating)
        return Response(serialized.data)

class WatchLaterViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.WatchLaterSerializer
    queryset = WatchLater.objects.all()
    def create(self, request):
        userId = request.user.id
        p_user = User.objects.filter(id=userId).first()
        movieId = request.data.get('movieId')
        p_movie = Movie.objects.filter(id=movieId).first()
        #p_dateSet = request.data.get('dateSet')
        newWatchLater = WatchLater(user = p_user, movie = p_movie)
        newWatchLater.save()
        serialized = self.get_serializer(newWatchLater)
        return Response(serialized.data)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        p_user = request.user
        self.perform_destroy(instance)
        return Response(None)
    @action(detail=False, methods=['GET'], name='GetByUser')
    def getByUser(self, request):
        p_user = request.user
        movieList = WatchLater.objects.filter(user=p_user)
        serialized = self.get_serializer(movieList, many=True)
        return Response(serialized.data)
