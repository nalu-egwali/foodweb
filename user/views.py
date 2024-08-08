
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# Create your views here.

def login_user (request):
    if request.method == 'POST':
        return HttpResponse("You are logged in")
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