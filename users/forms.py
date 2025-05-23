from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')