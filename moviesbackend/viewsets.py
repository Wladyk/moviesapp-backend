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

class WatchLaterViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.WatchLaterSerializer
    queryset = WatchLater.objects.all()
    def create(self, request):
        userId = request.data.get('userId')
        p_user = User.objects.filter(id=userId).first()
        movieId = request.data.get('movieId')
        p_movie = Movie.objects.filter(id=movieId).first()
        p_dateSet = request.data.get('dateSet')
        newWatchLater = WatchLater(user = p_user, movie = p_movie, dateSet = p_dateSet)
        newWatchLater.save()
        serialized = self.get_serializer(newWatchLater)
        return Response(serialized.data)
    @action(detail=False, methods=['GET'], name='GetByUser')
    def getByUser(self, request):
        #userId = request.data.get('userId')
        #p_user = User.objects.filter(id=userId).first()
        p_user = request.user
        movieList = WatchLater.objects.filter(user=p_user)
        serialized = self.get_serializer(movieList, many=True)
        return Response(serialized.data)