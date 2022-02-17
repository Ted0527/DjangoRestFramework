import json

from datetime import datetime

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication

from api.models import Point, Reward, TimeTable
from api.serializers import PointSerializer, RewardSerializer, TimeTableSerializer


# Create your views here.
class PointViewSet(ModelViewSet):
    
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    serializer_class = PointSerializer
    queryset = Point.objects.all()
    

class RewardViewSet(ModelViewSet):
    
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    serializer_class = RewardSerializer
    queryset = Reward.objects.all()
    
    
class TimeTableViewSet(ModelViewSet):
    
    permission_classes = [AllowAny]
    authentication_classes = [BasicAuthentication]
    serializer_class = TimeTableSerializer
    queryset = TimeTable.objects.all()