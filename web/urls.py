"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.api_views import GymViewSet, ProductViewSet, GymReviewViewSet

router = DefaultRouter()
router.register(r'gyms', GymViewSet)
router.register(r'products', ProductViewSet)
router.register(r'gym-reviews', GymReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),  
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', include("user.urls")), # login as default page
     path('gym_backend/', include('gym_backend.urls')),
     path('ai/', include('ai.urls')),

]
