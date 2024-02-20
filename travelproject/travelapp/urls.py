from django.contrib import admin
from django.urls import path

from travelapp import views

urlpatterns = [

    path('',views.travel1,name="travel"),
]
