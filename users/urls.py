from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    path("signup/",views.signupView,name = 'signup'),
    path("login/",views.loginView,name = 'login'),
    path("logout/",views.logoutView,name= 'logout'),
    path("account/",views.accountView,name = 'account')
]
