from django.contrib import admin
from .models import Meals, Booking, MasterTable

# Register your models here.

admin.site.register(Meals)
admin.site.register(Booking)
admin.site.register(MasterTable)
# admin.site.unregister(Meals)
# admin.site.unregister(Booking)

