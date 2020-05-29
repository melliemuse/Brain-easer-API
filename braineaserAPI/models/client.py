from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inner_child_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    # def __str__(self):
    #     return f'{self.user.first_name} {self.user.last_name}'
