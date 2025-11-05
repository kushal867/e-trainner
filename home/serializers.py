from rest_framework import serializers
from .models import Gym, Product, GymReview

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):  # fixed typo
    class Meta:
        model = Product
        fields = "__all__"

class GymReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymReview  # fixed model reference
        fields = "__all__"
