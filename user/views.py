
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_user (request):
    if request.method == 'POST':
        return HttpResponse("You are logged in")
    return render(request, 'loginform.html', {})

def logout_user (request):
    logout(request)
    return HttpResponse (" You are loggod out")