from django.contrib import admin
from shops.models import Category, Shop, Customer, Visited
# Register your models here.

admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Customer)
admin.site.register(Visited)