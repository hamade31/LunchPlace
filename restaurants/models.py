from django.db import models

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
    vote_count = models.PositiveSmallIntegerField()

class Address(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    building_name = models.CharField(max_length=100, null=true, blank=true)
    building_floor = models.CharField(max_length=100, null=true, blank=true)