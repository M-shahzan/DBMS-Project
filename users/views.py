from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import signupForm
from django.contrib import messages


# Create your views here.
def signupView(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()
            login(request,user)
            messages.success(request, "Signup successful! Welcome, " + user.username)
            return redirect("home")
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = signupForm()
    
    return render(request, "signup.html", {"form": form})

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect after login

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

def logoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return redirect("home")