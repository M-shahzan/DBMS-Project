from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import signupForm,UserUpdateForm
from django.contrib import messages
from reservation.models import Reservation


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
    logout(request)
    return redirect("home")

@login_required
def accountView(request):
    if request.method == 'POST':
        # Check which form was submitted
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            password_form = PasswordChangeForm(request.user)
            
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Your profile has been updated successfully.")
                return redirect('account')
            else:
                messages.error(request, "Please correct the errors below.")
                
        elif 'change_password' in request.POST:
            user_form = UserUpdateForm(instance=request.user)
            password_form = PasswordChangeForm(request.user, request.POST)
            
            if password_form.is_valid():
                user = password_form.save()
                # Prevent user from being logged out after password change
                update_session_auth_hash(request, user)
                messages.success(request, "Your password has been changed successfully.")
                return redirect('account')
            else:
                messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    # Get user's reservation history
    # Assuming you have a Reservation model with a user foreign key
    reservations = Reservation.objects.filter(user=request.user).order_by('-date')
    
    context = {
        'user_form': user_form,
        'password_form': password_form,
        # 'reservations': reservations
    }
    
    return render(request, 'account.html', context)