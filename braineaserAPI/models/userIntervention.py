from django.db import models
from braineaserAPI.models import Client, Intervention

class UserIntervention(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    anxiety_score = models.IntegerField()