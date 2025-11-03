from rest_framework import serializers
from .models import Gym, Product

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Gym
        fields = "__all__"

class PorductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        