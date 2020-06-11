from django.db import models
from braineaserAPI.models import Prompt, Client

class Journal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    entry = models.CharField(max_length=450)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)