from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    # Full name of the restaurant as it must show to the users or employees. I.e. not necessarily the legal name.
    name = models.CharField(max_length=100)
    # What sort of cuisine is this? e.g. Chinese, Fast-Food, India, mixed...etc.
    cuisine = models.CharField(max_length=100)

class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    # What day is the menu for?
    serving_date = models.DateField()
    # The actual menu is an image or a scan of an image that must be uploaded by the restaurant admin and stored by the back-end.
    menu_image = models.ImageField()
    # How many votes did this menu receive?
    # Assuming that the number of employees is typical of a small or medium business, 
    # so the max number of votes per menu will be in the hundreds.
    vote_count = models.PositiveSmallIntegerField()

class Address(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100, null=True, blank=True)
    building_floor = models.CharField(max_length=100, null=True, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

class RestaurantAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

# Everytime an employee votes, he or she gets 1 vote object created. 
# Ranked voting is also represented by a single vote object.
# This cannot be in the restaurants app due to circular import issue.
class Vote(models.Model):
    """
    This class represents voting in the system.
    """
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    # One vote per day per employee. The next day the employee can vote again.
    date = models.DateField()
    # 1 or more menus can be voted. Normally no more than 3 as per business rules, 
    # but this may change in the future.
    menus = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False)