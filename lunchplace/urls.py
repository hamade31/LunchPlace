from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from voting.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('employees', EmployeeViewSet)
router.register('restaurantadmins', RestaurantAdminViewSet)
router.register('addresses', AddressViewList)
router.register('restaurants', RestaurantViewList)
router.register('menus', MenuViewList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]