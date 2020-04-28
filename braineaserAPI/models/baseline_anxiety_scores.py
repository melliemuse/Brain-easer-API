from django.db import models
from braineaserAPI.models.clients import Clients

class BaselineAnxietyScores(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    anxietyScore = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.CharField(max_length=250)