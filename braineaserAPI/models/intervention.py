from django.db import models

class Intervention(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=650)
    icon = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    instructions = models.CharField(max_length=650)
    detailed_info = models.CharField(max_length=650, default=None, blank=True, null=True)