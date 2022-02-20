from django.contrib import admin
from users.models import CustomAccounts

# Register your models here.
admin.site.register(CustomAccounts)

# @admin.register(CustomAccounts)
# class CustomAccountsAdmin(admin.ModelAdmin):
#   list_display = ['id', 'email', 'password']
#   list_display_links = ['id', 'email', 'password']
#   search_fields = ['shop_name', ]
