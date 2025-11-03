from rest_framework import viewsets
from .models import Gym
from serializers import GymSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    
    