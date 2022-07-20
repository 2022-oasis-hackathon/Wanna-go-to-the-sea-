from django.contrib import admin
from my_app.models import house, recommend_place, region_detail_page, experience_detail_page, login_data


# Register your models here.

admin.site.register(house)
admin.site.register(recommend_place)
admin.site.register(region_detail_page)
admin.site.register(experience_detail_page)
admin.site.register(login_data)