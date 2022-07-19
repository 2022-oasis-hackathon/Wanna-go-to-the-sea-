from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'my_app'

urlpatterns = [
    path('', views.mainpage, name ='mainpage'),
    path('experience/', views.experience, name ='experience'),
    path('spotmap/', views.spotmap, name ='spotmap'),
    path('<topic>', views.detail),
]