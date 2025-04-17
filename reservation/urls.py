from django.contrib import admin
from django.urls import path
from .views import reserveView,tablesView
 
urlpatterns = [

    path('reserve/',reserveView,name='reserve'),
    path('tables/',tablesView,name = 'table_view'),
]