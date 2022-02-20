from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models   import Sum, Avg

class Teacher(models.Model):
    name = models.CharField(max_length=25)
    
    class Meta:
        db_table = 'teachers'
        
    def __str__(self):
        return self.name
        
class Student(models.Model):
    name    = models.CharField(max_length=25)
    email   = models.EmailField(max_length=254)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'students'
    

class Score(models.Model):
    student = models.ForeignKey('Student', on_delete=CASCADE)
    korean = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    
    class Meta:
        db_table = 'score'