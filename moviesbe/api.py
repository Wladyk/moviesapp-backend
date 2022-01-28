from rest_framework import routers
from moviesbackend import viewsets
router = routers.DefaultRouter()
router.register(r'user', viewsets.UserViewset, basename="user")
router.register(r'movie', viewsets.MovieViewset, basename="movie")
router.register(r'genre', viewsets.GenreViewset, basename="genre")
router.register(r'movie', viewsets.MovieViewset, basename="movie")
router.register(r'watchlater', viewsets.WatchLaterViewset, basename="watchlater")
router.register(r'rating', viewsets.RatingViewset, basename="rating")