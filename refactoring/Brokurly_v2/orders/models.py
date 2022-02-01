from django.db import models

from .models import Product, User, TimeStampModel


class OrderStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Order(TimeStampModel):
    order_number = models.CharField(max_length=150)
    users        = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number


class OrderItemsStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class OrderItem(TimeStampModel):
    tracking_number    = models.CharField(max_length=200,null=True)
    quantity           = models.IntegerField()
    order              = models.ForeignKey('Order', on_delete=models.CASCADE)
    product            = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_items_status = models.ForeignKey('OrderItemsStatus', on_delete=models.CASCADE)

    def __str__(self):
        return self.tracking_number