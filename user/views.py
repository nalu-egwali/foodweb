
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

def login_user (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            return HttpResponse("Login Error")
    return render(request, 'loginform.html', {})

def logout_user (request):
    logout(request)
    return HttpResponse ("You are loggod out")

def signup (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
        else:
            return HttpResponse('There was an error in your input')
    else:    
        form = SignUpForm()
        return render (request, 'signup.html', {'form': form})