# from rest_framework_simplejwt.views  import TokenViewBase, TokenVerifyView
from rest_framework import viewsets
from rest_framework import serializers

from users.serializers import CustomAccountsSerializer
from users.models import CustomAccounts


class CustomAccountsViewSet(viewsets.ModelViewSet):
    queryset = CustomAccounts.objects.all()
    serializer_class = CustomAccountsSerializer