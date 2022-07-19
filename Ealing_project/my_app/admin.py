from django.contrib import admin
from my_app.models import house, recommend_place


# Register your models here.

admin.site.register(house)
admin.site.register(recommend_place)