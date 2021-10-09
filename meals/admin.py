from django.contrib import admin
from .models import Meals, Reserve, MasterTable

# Register your models here.
admin.site.register(Meals)
admin.site.register(Reserve)
admin.site.register(MasterTable)
# admin.site.unregister(Meals)
# admin.site.unregister(Reserve)
