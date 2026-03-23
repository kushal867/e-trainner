from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import GymViewSet, ProductViewSet, GymReviewViewSet

router = DefaultRouter()

# Use plural names (REST best practice)
router.register(r'gyms', GymViewSet, basename='gym')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', GymReviewViewSet, basename='review')

urlpatterns = [
    path('api/', include(router.urls)),
]
