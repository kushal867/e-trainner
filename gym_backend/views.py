from django.shortcuts import render
from .models import Gym  # assuming your Gym model exists

def gym_location_map(request):
    gyms = Gym.objects.all()
    return render(request, 'gym_location_map.html', {'gyms': gyms})
