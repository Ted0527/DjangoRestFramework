from rest_framework import serializers
from users.models import CustomAccounts


class CustomAccountsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomAccounts
        fields = "__all__"