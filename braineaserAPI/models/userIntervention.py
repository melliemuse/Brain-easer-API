from django.db import models
from braineaserAPI.models import Client, Intervention

class UserIntervention(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)