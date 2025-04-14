from django.contrib import admin
from django.urls import path
from .views import menuView
 
urlpatterns = [
    path('menu/',menuView,name='menu')
]