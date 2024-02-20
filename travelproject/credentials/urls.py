from django.contrib import admin
from django.urls import path,include

from credentials import views
app_name = 'credentials'

urlpatterns = [
     path('register/',views.register, name="reg"),
     path('login/', views.login,name='login'),
     path('logout/', views.logout,name='logout'),
]