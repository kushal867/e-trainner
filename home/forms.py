from django import forms
from .models import Gym, Product, GymReview

#for GymForm
class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = "__all__"

#form ProductForm
class ProductForm(forms.ModelForm):
    class Meta:
        model =  Product
        fields = "__all__"

#for GymReview
class GymReviewForm(forms.ModelForm):
    class Meta:
        models = GymReview
        fields = "__all__"
