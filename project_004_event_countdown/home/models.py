from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=256)
    event_datetime = models.DateTimeField()
