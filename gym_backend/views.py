from django.shortcuts import render
from .models import Gym
from django.core.serializers import serialize

def gym_location_map(request):
    gyms = Gym.objects.all()
    gyms_json = serialize('json', gyms)  # converts queryset to JSON
    return render(request, 'gym_location_map.html', {'gyms_json': gyms_json})
