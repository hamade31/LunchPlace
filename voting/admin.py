from django.contrib import admin
from voting.models import *

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Address)
admin.site.register(Employee)
admin.site.register(RestaurantAdmin)
admin.site.register(Vote)