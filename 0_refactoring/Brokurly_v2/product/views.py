from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from product.models import Menu, Category, Product
from product.serializers import MenuSerializer, CategorySerializer, ProductSerializer


class MenuViewSet(ModelViewSet):
    
    permission_class = [AllowAny]
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()


class CategoryViewSet(ModelViewSet):
    
    permission_class = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(ModelViewSet):
    
    permission_class = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    