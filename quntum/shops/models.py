from django.db import models

class Category(models.Model): # 한식, 일식, 중식, 양식
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Visited(models.Model):
    visited_time = models.DateTimeField()
    shop         = models.ForeignKey(Shop, on_delete=models.CASCADE)
    customer     = models.ForeignKey(Customer, on_delete=models.CASCADE)  