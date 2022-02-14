from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, TagViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='Product')
router.register(r'tag', TagViewSet, basename='tag')

urlpatterns = [
    
] + router.urls