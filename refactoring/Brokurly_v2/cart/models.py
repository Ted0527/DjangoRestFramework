from django.db import models

from product.models import Product
from users.models import CustomAccounts
from core.models import TimeStampModel


class Cart(TimeStampModel):
    quantity = models.IntegerField(default=0)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    user     = models.ForeignKey(CustomAccounts, on_delete=models.CASCADE)