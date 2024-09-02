from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from foods.models import Food

# Create your views here.

@login_required
def index(request):
    foods = Food.objects.filter(created_by = request.user)
    return render (request, 'dashboard/index.html', {'foods': foods})