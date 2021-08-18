from django.contrib.auth.models import User, Group
from rest_framework import serializers
from voting.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'employee', 'restaurantadmin']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class RestaurantAdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantAdmin
        fields = '__all__'

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'cuisine']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['restaurant', 'serving_date', 'menu_image', 'vote_count']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['restaurant', 'area', 'street', 'postal_code', 'building_name', 'building_floor']