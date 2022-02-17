from django.contrib import admin

from api.models import Point, Reward, TimeTable
# Register your models here.

admin.site.register(Point)
admin.site.register(Reward)
admin.site.register(TimeTable)