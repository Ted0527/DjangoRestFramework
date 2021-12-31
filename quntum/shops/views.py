from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from shops.serializers import CategorySerializer, ShopSerializer, CustomerSerializer, VisitedSerializer
from shops.models import Category, Shop, Customer, Visited

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ShopModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()



# class ShopModelViewSet(viewsets.ModelViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = ShopSerializer
    
#     def list(self, request):
#         queryset = Shop.objects.all()
#         serializer = ShopSerializer(queryset)
#         return Response(serializer.data)
    
#     def retrieve(self, request, pk):
#         queryset = Shop.objects.get(pk=pk)
#         serializer = ShopSerializer(queryset)
#         return Response(serializer.data)
    

class CustomerModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class VisitedModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = VisitedSerializer
    queryset = Visited.objects.all()