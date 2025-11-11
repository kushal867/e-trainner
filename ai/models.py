from django.db import models
from home.models import Gym

class GymDoc(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='gym_pdfs/')
    extracted_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gym.name} PDF"
