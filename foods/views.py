from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import NewFoodForm
from .models import Food
from . import urls


# Create your views here.
def index (request):
    foods = Food.objects.all()
    return render(request, 'home.html', {'foods': foods,})

def get_details (request, food_id):
    food = get_object_or_404(Food, pk = food_id)
    related_foods = Food.objects.filter(category = food.category, is_sold = False).exclude(pk = food.id)[0:4]

    return render(request, 'details.html', {
        'food': food,
        'related_foods': related_foods
    })

# Add new food item
@login_required (login_url='/user/login') # add login redirect to bypass django built-in login redirect
def new_food (request):
    # If the user submits the form, process the form
    if request.method == 'POST':
        form = NewFoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.creadted_by = request.user
            food.save()
            return redirect('food:details', pk=food.id)
        else:
            return render (request, 'newfood.html', {'form': form})
    
    # Else just show the user a form to fill
    form = NewFoodForm()
    return render(request, 'newfood.html', {'form': form})
