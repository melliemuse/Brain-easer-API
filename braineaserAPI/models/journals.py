from django.db import models
from braineaserAPI.models import Prompts, Clients

class Journals(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    entry = models.CharField(max_length=450)
    prompt = models.ForeignKey(Prompts, on_delete=models.CASCADE)