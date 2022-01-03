from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from shops.serializers import CategorySerializer, ShopSerializer, CustomerSerializer, VisitedSerializer
from shops.models import Category, Shop, Customer, Visited

class CategoryModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# class ShopModelViewSet(ModelViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = ShopSerializer
#     queryset = Shop.objects.all()



class ShopModelViewSet(ModelViewSet):
    def list(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        object = Shop.objects.get(pk=pk)
        serializer = ShopSerializer(object)
        return Response(serializer.data)
    
    def update(self, request, pk):
        object = Shop.objects.get(pk=pk)
        shop = request.data
        serializer = ShopSerializer(object, shop)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def partial_update(self, request, pk):
        object = Shop.objects.get(pk=pk)
        shop = request.data
        serializer = ShopSerializer(object, shop)
        if  serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        object = Shop.objects.get(pk=pk)
        object.delete()
        return Response({'result':'Delete completed'})

class CustomerModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class VisitedModelViewSet(ModelViewSet):
    permission_classes = [AllowAny] 
    serializer_class = VisitedSerializer
    queryset = Visited.objects.all()