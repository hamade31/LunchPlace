from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class RestaurantAdmin(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)