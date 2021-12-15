from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path("about",views.about,name='about'),
    path("Srobot",views.Srobot,name='Srobot'),
    path("cyberWarfare",views.cyberWarfare,name='cyberWarfare'),
    path("Uav",views.Uav,name='Uav'),


]


