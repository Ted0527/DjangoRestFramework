from django.db import models

# Create your models here.
class Point(models.Model):
    point = models.IntegerField(default=0)
    
    
class Reward(models.Model):
    reward = models.CharField(max_length=255)
    
    
class TimeTable(models.Model):
    time = models.CharField(max_length=50)