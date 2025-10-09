# url/models.py
from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=200)  # Store the original URL
    slug = models.CharField(max_length=15)  # Store the shortened slug

    def __str__(self):
        return f"Short URL for: {self.url} is {self.slug}"
