from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'food'
urlpatterns = [
    path("", views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('<int:food_id>/', views.get_details, name='details' )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)