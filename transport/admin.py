from django.contrib import admin
from .models import Profile, Ride

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'phone', 'address')

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('customer', 'driver', 'status', 'pickup', 'dropoff', 'price')
