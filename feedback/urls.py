from django.contrib import admin
from django.urls import path
from .views import feedbackView,feedbackListView
 
urlpatterns = [
    path('feedback/',feedbackView,name = 'feedback'),
    path('feedbackList/',feedbackListView,name = 'feedbackList'),
]