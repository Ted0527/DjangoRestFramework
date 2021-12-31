from shops.models       import Category, Shop, Customer, Visited
from rest_framework     import serializers
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    shop_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_shop_name(self, data):
        shop = data.shop_set.all()
        return shop.values()

class ShopSerializer(ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    customer_total = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = '__all__'

    def get_customer_name(self, data):
        return set([visitor.customer.name for visitor in data.visited_set.all()])
    
        # visitors = [i.visited_set.all() for i in data]
        # customer_id = set([visitor.filter() for visitor in visitors])
        # customer = Customer.objects.get(id=customer_id)
        # result=[set([visitors.customer.name for visitors in shop.visited_set.all()]) for shop in data]
        # return result

    def get_customer_total(self, data):
        customer = Visited.objects.filter(shop_id = data.id).count()
        return customer
    
class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class VisitedSerializer(ModelSerializer):
    # visited_shop = serializers.SerializerMethodField()

    class Meta:
        model = Visited
        fields = '__all__'