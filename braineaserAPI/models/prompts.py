from django.db import models

class Prompts(models.Model):
    prompt = models.CharField(max_length=500)