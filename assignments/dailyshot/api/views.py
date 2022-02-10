from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProductsSerializer
# Create your views here.

class ProductsViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer
    