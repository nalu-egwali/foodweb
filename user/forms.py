
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm (UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter a Username',
        'class': 'w-full py-2 px-3 rounded-xl bg-gray-400 text-white'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter an Email',
        'class': 'w-full py-2 px-3 rounded-xl bg-gray-400 text-white'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-2 px-3 rounded-xl bg-gray-400 text-white'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full py-2 px-3 rounded-xl'
    }))