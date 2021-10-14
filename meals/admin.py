"""
for superUser
"""
from django.contrib import admin
from .models import Meals, Booking

# Register your models here.

admin.site.register(Meals)
admin.site.register(Booking)
