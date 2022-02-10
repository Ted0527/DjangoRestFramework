from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import ProductsViewSet

router = DefaultRouter(trailing_slash=True)

router.register(r'product', ProductsViewSet, basename='Product')

urlpatterns = [
    
] + router.urls