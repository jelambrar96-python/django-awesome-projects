from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100, default='something')
    description = models.CharField(max_length=100, default='something')