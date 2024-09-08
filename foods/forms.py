
from django import forms

from .models import Food

class NewFoodForm (forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter food category',
        'class': 'w-full py-2 px-3 rounded-xl '
    }))

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Food Name',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'w-full py-2 px-3 rounded-xl',
        'rows': '4'
    }))

    image = forms.FileInput()

    price = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter food price',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    class Meta:
        model= Food
        fields= ('category', 'name', 'description', 'image', 'price') 

class EditFoodForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Food Name',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Description',
        'class': 'w-full py-2 px-3 rounded-xl',
        'rows': '4'
    }))

    image = forms.FileInput()

    price = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Enter food price',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))

    class Meta:
        model= Food
        fields= ('category', 'name', 'description', 'image', 'price')