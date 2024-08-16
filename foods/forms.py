
from django import forms

from .models import Food

class NewFoodForm (forms.ModelForm):
    class Meta:
        model= Food
        fields= ('category', 'name', 'description', 'image', 'price') 