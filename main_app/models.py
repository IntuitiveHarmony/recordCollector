from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    trackList = ArrayField(
        models.CharField(max_length=50)
    )