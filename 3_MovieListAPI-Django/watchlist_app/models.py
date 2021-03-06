from django.db import models
from django.db.models.fields import related
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=255)
    
    class Meta:
        db_table = 'platforms'
    
    def __str__(self):
        return self.name
    
class Watchlist(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'watchlists'

    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)
    
    
class User(models.Model):
    name = models.CharField(max_length=50)
    
    
class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class PointInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point_log = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)