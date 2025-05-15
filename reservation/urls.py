from django.contrib import admin
from django.urls import path
from .views import reserveView,tablesView,feedbackView,feedbackListView
 
urlpatterns = [

    path('reserve/',reserveView,name='reserve'),
    path('tables/',tablesView,name = 'tables'),
    path('feedback/',feedbackView,name = 'feedback'),
    path('feedbackList/',feedbackListView,name = 'feedbackList'),
]