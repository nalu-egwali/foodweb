from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Food
from . import urls

# Create your views here.
def index (request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods,})

def get_details (request, food_id):
    food = get_object_or_404(Food, pk = food_id)
    related_foods = Food.objects.filter(category = food.category, is_sold = False).exclude(pk = food.id)[0:3]

    return render(request, 'details.html', {
        'food': food,
        'related_foods': related_foods
    })

def login_user (request):
    if request.method == 'POST':
        return HttpResponse("You are logged in")
    return render(request, 'loginform.html', {})

def logout_user (request):
    logout(request)
    return HttpResponse (" You are loggod out")
