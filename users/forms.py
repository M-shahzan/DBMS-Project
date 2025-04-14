from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        fields = ['username','email','password1','password2']