from django.urls import path
from .views import (
    gym_list, gym_create, gym_edit, gym_delete,
    product_create, product_edit, product_delete, product_list,
    gym_review_list, gymReview_create, gymReview_edit, gymReview_delete
)

urlpatterns = [
    # Gym URLs
    path('', gym_list, name='gym_list'),
    path('create/', gym_create, name='gym_create'),
    path('edit/<int:id>/', gym_edit, name='gym_edit'),
    path('delete/<int:id>/', gym_delete, name='gym_delete'),

    # Product URLs
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:id>/edit/', product_edit, name='product_edit'),
    path('products/<int:id>/delete/', product_delete, name='product_delete'),

    # Gym Review URLs
    path('gymReview/', gym_review_list, name='gymReview_list'),
    path('gymReview/create/', gymReview_create, name='gymReview_create'),
    path('gymReview/<int:id>/edit/', gymReview_edit, name='gymReview_edit'),
    path('gymReview/<int:id>/delete/', gymReview_delete, name='gymReview_delete'),
]
