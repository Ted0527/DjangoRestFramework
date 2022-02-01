from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shops.views import CategoryModelViewSet, ShopModelViewSet, CustomerModelViewSet, VisitedModelViewSet



router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'shop', ShopModelViewSet, basename='shop')
router.register(r'customer', CustomerModelViewSet, basename='customer')
router.register(r'visited', VisitedModelViewSet, basename='visited')


# category_list = CategoryModelViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create',
# })

# category_detail = CategoryModelViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

# shop_list = ShopModelViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })

# shop_detail = ShopModelViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

# customer_list = CustomerModelViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })

# customer_detail = CustomerModelViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

# visited_list = VisitedModelViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })

# visited_detail = VisitedModelViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })

urlpatterns = [
    path('', include(router.urls))
    # path('category', category_list),
    # path('category/<int:pk>', category_detail),
    # path('shop', shop_list),
    # path('shop/<int:pk>', shop_detail),
    # path('customer', customer_list),
    # path('customer/<int:pk>', customer_detail),
    # path('visited', visited_list),
    # path('visited/<int:pk>', visited_detail),
]