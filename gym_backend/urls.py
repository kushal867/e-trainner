from django.urls import path
from . import views 

urlpatterns = [
    path('locations/', views.gym_location_map, name='gym_location_map'),
]
