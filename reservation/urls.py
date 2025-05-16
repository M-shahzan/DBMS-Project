from django.contrib import admin
from django.urls import path
from .views import reserveView,tablesView,reservationsView
 
urlpatterns = [

    path('reserve/',reserveView,name='reserve'),
    path('tables/',tablesView,name = 'tables'),
    path('reservations/',reservationsView,name = 'reservations')

]