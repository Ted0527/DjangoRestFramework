from rest_framework.serializers import ModelSerializer, SerializerMethodField

from product.models import Menu, Category, Product, Image


class MenuSerializer(ModelSerializer):
    
    class Meta:
        model = Menu
        fields = '__all__'
        
        
class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductSerializer(ModelSerializer):
    image = SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_image(self, data):
        return Image.objects.filter(product_id = data.id).values()