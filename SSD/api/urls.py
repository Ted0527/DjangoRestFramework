from django.urls import path

from api.views import PointViewSet, RewardViewSet, TimeTableViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'point', PointViewSet, basename='Point')
router.register(r'reward', RewardViewSet, basename='Reward')
router.register(r'timetable', TimeTableViewSet, basename='Timetable')

urlpatterns = [ ] + router.urls