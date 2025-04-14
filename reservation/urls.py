from django.contrib import admin
from django.urls import path
from .views import reserveView
 
urlpatterns = [

    path('reserve/',reserveView,name='reserve'),
]