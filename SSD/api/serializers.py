from api.models import Point, Reward, TimeTable

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class PointSerializer(ModelSerializer):
    
    class Meta:
        model = Point
        fields = '__all__'
        
        
class RewardSerializer(ModelSerializer):
    
    class Meta:
        model = Reward
        fields = '__all__'
        
        
class TimeTableSerializer(ModelSerializer):
    
    class Meta:
        model = TimeTable
        fields = '__all__'