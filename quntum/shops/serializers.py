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

class ShopSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    customer_total = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = '__all__'

    def get_customer_name(self, data):
        return set([visitor.customer.name for visitor in data.visited_set.all()])
    
        # customer = set([visitor.customer.name for visitor in data.visited_set.all()])
        # return customer
        # visitors = Visited.objects.filter(customer_id = data.id).select_related('customer')
        # customers = [[a.customer.name for a in i] for i in visitors]
        # result=[[visitors.customer.name for visitors in shop.visited_set.all()] for shop in data]

    def get_customer_total(self, data):
        customer = Visited.objects.filter(shop_id = data.id).count()
        return customer
    #     visitors = Visited.objects.filter(shop_id = data.id)
    #     customers = [i.customer_id for i in visitors]
    #     return len(set(customers))
    
class CustomerSerializer(ModelSerializer):
    visited_shops = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'
    
    def get_visited_shops(self, data):
        return Visited.objects.filter(customer_id = data.id).values()
        # print(data)
        # results = [{
        #     'id' : i.id,
        #     'shop_id' : i.shop_id,
        #     'visited_time' : i.visited_time,
        #     'customer_id' : i.customer_id,
        # }for i in data.visited_set.all()]
        
        # return results
        
        # shops_name = [customer.shop.name for customer in data.visited_set.all()]
        # visited_time = [i.visited_time for i in data.visited_set.all()]
        # return visited_time, shops_name



class VisitedSerializer(ModelSerializer):

    class Meta:
        model = Visited
        fields = '__all__'