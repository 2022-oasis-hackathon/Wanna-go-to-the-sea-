from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'my_app'

urlpatterns = [
    path('', views.mainpage, name ='mainpage'),
    path('logout/', views.logout, name ='logout'),
    path('home/', views.home, name ='home'),
    path('start/login/', views.login, name ='login'),
    path('experience/', views.experience, name ='experience'),
    path('spotmap/', views.spotmap, name ='spotmap'),
    path('<topic>', views.detail, name = 'detail'),
    path('ex_detail/', views.ex_detail, name ='ex_detail'),
]