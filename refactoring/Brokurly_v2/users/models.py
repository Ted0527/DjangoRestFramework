from django.db   import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as lazy

from core.my_user import CustomUserManager


class CustomAccounts(AbstractUser):
    username  = None
    email     = models.EmailField(lazy('email address'), unique=True)
    address   = models.TextField()
    contact   = models.CharField(max_length=200)
    spouse_name = models.CharField(max_length=100, blank=True)
    data_of_birth = models.DateField(blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()


    def __str__(self):
        return self.email