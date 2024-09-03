
from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('food/<int:pk>/', views.delete_food, name='delete_food'),
]