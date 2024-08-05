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
