from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50)
    thumbnail_image = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    list_price = models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    tag = models.CharField(max_length=10)

class ProductTag(models.Model):
    product = models.ManyToManyField(Product)
    tag = models.ManyToManyField(Tag)