from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 50)
    thumbnail_image = models.URLField()
    price = models.IntegerField(default=0)
    list_price = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default = True)
    tag = models.CharField(max_length=10, blank = True)
    
    def __str__(self):
        return self.name