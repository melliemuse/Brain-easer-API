from django.db import models
from braineaserAPI.models.client import Client

class BaselineAnxietyScore(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    anxietyScore = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.CharField(max_length=250)