import math

from rest_framework import serializers as sz
from rest_framework.serializers import ModelSerializer as MSZ

from api.models import Product, Tag


class ProductSerializer(MSZ):
    discount_rate = sz.SerializerMethodField()
    tag = sz.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='tag'
    )
    
    class Meta:
        model = Product
        fields = ['name', 'thumbnail_image', 'price', 'list_price', 'out_of_stock', 'tag', 'discount_rate']
        
    def get_discount_rate(self, data):
        price = data.price
        list_price = data.list_price
        
        discount_rate = math.trunc((1 - price/list_price) * 100)
        return discount_rate
    

class TagSerializer(MSZ):
    
    class Meta:
        model = Tag
        fields = ['tag']