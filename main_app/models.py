from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    # why does null work in python?
    releaseDate = models.DateField(null=True)
    trackList = ArrayField(
        models.CharField(max_length=50)
    )