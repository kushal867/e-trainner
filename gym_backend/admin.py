from django.contrib import admin
from .models import Gym

@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'country', 'latitude', 'longitude')
    search_fields = ('name', 'city', 'state', 'country')
    list_filter = ('city', 'state', 'country')
