from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self) :
        return self.name




class Food(models.Model):
    category = models.ForeignKey(Category, related_name="foods", on_delete=models.CASCADE )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="food_images", blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name="foods", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
