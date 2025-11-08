from django.shortcuts import render, redirect
from .models import Gym
from .forms import GymForm
from django.core.serializers import serialize

# Create your views here.
def gym_location_map(request):
    gyms = Gym.objects.all()
    gyms_json = serialize('json', gyms)  # convert queryset to JSON
    return render(request, 'gym_location_map.html', {'gyms_json': gyms_json})



