from django import forms
from .models import Gym

class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        fields = "__all__"