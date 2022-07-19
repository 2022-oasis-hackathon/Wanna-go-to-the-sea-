from django.contrib import admin
from my_app.models import house, recommend_place, region_detail_page


# Register your models here.

admin.site.register(house)
admin.site.register(recommend_place)
admin.site.register(region_detail_page)