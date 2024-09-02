
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("foods.urls")),
    path('user/', include('user.urls')),
    path('food/', include('foods.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
