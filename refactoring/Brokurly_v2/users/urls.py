from django.urls import path, include
from rest_framework import routers
from users.views import CustomAccountsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=True)
router.register(r'', CustomAccountsViewSet)


urlpatterns = [
    # path('', include(router.urls)),
] + router.urls