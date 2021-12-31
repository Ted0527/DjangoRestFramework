from django.urls import path
from shops.views import CategoryModelViewSet, ShopModelViewSet, CustomerModelViewSet, VisitedModelViewSet

category_list = CategoryModelViewSet.as_view({
    'get' : 'list',
    'post' : 'create',
})

category_detail = CategoryModelViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

shop_list = ShopModelViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

shop_detail = ShopModelViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

customer_list = CustomerModelViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

customer_detail = CustomerModelViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

visited_list = VisitedModelViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

visited_detail = VisitedModelViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('category', category_list),
    path('category/<int:pk>', category_detail),
    path('shop', shop_list),
    path('shop/<int:pk>', shop_detail),
    path('customer', customer_list),
    path('customer/<int:pk>', customer_detail),
    path('visited', visited_list),
    path('visited/<int:pk>', visited_detail),
]