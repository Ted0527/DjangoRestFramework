from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response    import Response
from rest_framework import serializers, status


from api.serializers import ProductSerializer, TagSerializer
from api.models import Product, Tag
# Create your views here.


class ProductViewSet(ModelViewSet):
    
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def create(self, request):
        data = request.data

        print(data['price'])
        print(data['list_price'])
        # if data['price'] or data['list_price'] < 0:
        #     return Response({'result' : '양수로 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if data['price'] > data['list_price']:
            return Response({'result' : '상품가격은 정가보다 클 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.data)

    # def retrieve(self, request, pk):
    #     product = Product.objects.get(pk=pk)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
            
    def partial_update(self, request, pk):
        obj = Product.objects.get(pk=pk)
        new_value = request.data
        serializer = ProductSerializer(obj, new_value)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def destroy(self, request, pk=None):
        product = Product.objects.filter(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class TagViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    
    