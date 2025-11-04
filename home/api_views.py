from rest_framework import viewsets
from .models import Gym, Product, GymReview
from serializers import GymSerializer, PorductSeraializer, GymReviewSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PorductSeraializer

class Gymviewset(viewsets.ModelViewSet):
    queryclass = GymReview.objects.all()
    serializer_class = GymReviewSerializer
    