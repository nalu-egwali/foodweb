from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import urls

# Create your views here.
def index (request):
    return render(request, 'home.html', {})

def login_user (request):
    if request.method == 'POST':
        return HttpResponse("You are logged in")
    return render(request, 'loginform.html', {})

def logout_user (request):
    logout(request)
    return HttpResponse (" You are loggod out")
