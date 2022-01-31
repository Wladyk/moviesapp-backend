from django.db import models 
import datetime
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg

#The Genre model will be used to provide a customizable list of gendres for each movie
class Genre(models.Model):
    name = models.CharField(max_length=200, default="No name")
    description = models.TextField(default="No description")
    def __str__(self):
        return str(self.id) + "-" + self.name

class Movie(models.Model):
    title = models.CharField(max_length=200, default="No title")
    releaseDate = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT) #we cannot destroy genres
    #id there're still movies assigned to them
    plot = models.TextField(default="No plot")
    @property
    def averageRating(self):
        if hasattr(self, '_averageRating'):
            return self._averageRating
        return self.ratings.aggregate(Avg('rating'))
    def __str__(self):
        return str(self.id) + "-" + self.title 

#new user model has been defined to account for the "Watch later list"
class User(AbstractUser):
    watchLaterList = models.ManyToManyField(Movie, through="WatchLater")
    def __str__(self):
        return str(self.id) +"-"+ self.username

#this "intersection" model provides the link between "User" and "Movie"
# we could use the implicit model created by Django on the ManyToManyField
#but I wanted to add date
class WatchLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    dateSet = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+"-"+self.user.username+"-"+self.movie.title
    class Meta:
        unique_together = ('user','movie') #So a same user cannot put the movie in his watch later twice

#Ratings may be given to a movie by a certain user
class Rating(models.Model):
    class GivenRating(models.IntegerChoices):
        HORRIBLE = 1
        BAD = 2
        ACCEPTABLE = 3
        GOOD = 4
        EXCELLENT = 5
    rating = models.IntegerField(choices=GivenRating.choices)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #if an author gets deleted, the ratings she/he gave will still remain
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    #deleting a movie will also delete all the ratings associated to it
    message = models.TextField(default="No comments")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Rating ID: " + str(self.id)