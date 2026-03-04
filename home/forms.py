from django import forms
from .models import Gym, Product, GymReview


class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = [
            "name",
            "location",
            "description",
            "price",
            "image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "price": forms.NumberInput(attrs={"min": 0}),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "gym",
            "price",
            "stock",
            "description",
            "image",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "price": forms.NumberInput(attrs={"min": 0}),
            "stock": forms.NumberInput(attrs={"min": 0}),
        }

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock is not None and stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock


class GymReviewForm(forms.ModelForm):
    class Meta:
        model = GymReview
        fields = [
            "gym",
            "user",
            "rating",
            "comment",
        ]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating and not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
