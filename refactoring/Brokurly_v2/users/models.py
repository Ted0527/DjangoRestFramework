from django.db   import models

from .models import TimeStampModel


class User(TimeStampModel):
    name      = models.CharField(max_length=50)
    email     = models.EmailField(max_length=200, unique=True)
    address   = models.TextField()
    contact   = models.CharField(max_length=200)
    username  = models.CharField(max_length=50, unique=True)
    password  = models.CharField(max_length=250)

    def __str__(self):
        return self.username