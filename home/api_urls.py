
from api_views import GymViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gym', GymViewSet, basename='gym')

urlpatterns = router.urls
