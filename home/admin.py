from django.contrib import admin
from .models import Gym, Product, GymReview

# Gym Admin
@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'price_per_month', 'contact_number', 'created_at')
    search_fields = ('name', 'address')
    list_filter = ('price_per_month',)
    ordering = ('name',)

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'gym', 'price', 'stock', 'created_at')
    search_fields = ('name', 'gym__name')
    list_filter = ('gym', 'price')
    ordering = ('name',)

# Gym Review Admin
@admin.register(GymReview)
class GymReviewAdmin(admin.ModelAdmin):
    list_display = ('gym', 'user', 'rating', 'created_at')
    search_fields = ('gym__name', 'user__username')
    list_filter = ('rating',)
    ordering = ('-created_at',)
