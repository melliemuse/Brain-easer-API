from django.db import models
from braineaserAPI.models import Clients, Interventions

class UserInterventions(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)
    intervention = models.ForeignKey(Interventions,  on_delete=models.CASCADE)