from rest_framework import viewsets
from .models import Gym, Product, GymReview
from .serializers import GymSerializer, ProductSerializer, GymReviewSerializer

class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class GymReviewViewSet(viewsets.ModelViewSet):
    queryset = GymReview.objects.all()
    serializer_class = GymReviewSerializer
