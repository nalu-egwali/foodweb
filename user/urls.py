
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('logout', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
]