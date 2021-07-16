from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def login(request):
    error = ''
    if request.user.is_authenticated:
        return redirect('core:calculation')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # authenticate user's, email and password
        print(user, "----->")
        if user is not None:
            auth_login(request, user)
            return redirect('core:calculation')
        else:
            error = 'Invalid Username or Password'
            form = AuthenticationForm(request.POST)
            return render(request, 'accounts/login.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('core:calculation')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
