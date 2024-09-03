from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from foods.models import Food

# Create your views here.

@login_required
def index(request):
    foods = Food.objects.filter(created_by = request.user)
    return render (request, 'dashboard/index.html', {'foods': foods})

@login_required
def delete_food(request, pk):
    food_item = get_object_or_404(Food, pk, created_by = request.user)
    food_item.delete()

    return redirect('/dashboard/index/')