from django.db import models

from .models import Product, User, TimeStampModel


class Cart(TimeStampModel):
    quantity = models.IntegerField(default=0)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)