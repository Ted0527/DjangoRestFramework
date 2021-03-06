"""Brokurly_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url


urlpatterns = [
    path('admin', admin.site.urls),
    path('token', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name = 'token_verify'),
    url(r'^rest-auth', include('dj_rest_auth.urls')),
    url(r'^rest-auth/registration', include('dj_rest_auth.registration.urls')),
    url(r'^users', include('allauth.urls')),
    url(r'^users', include('users.urls')),
    #url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    # path('users', include('dj_rest_auth.urls')),
    # path('users', include('dj_rest_auth.registration.urls')),
    # path('users', include('allauth.urls')),
    # path('users', include('users.urls')),
    # path('product', include('product.urls')),
    # path('order', include('orders.urls')),
    # path('cart', include('cart.urls'))
]