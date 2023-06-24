from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class Instrument(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    quote = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=250)
    # Artists relationship many to many
    artists = models.ManyToManyField(Artist)
    # Override the __str method so the object in the ORM has a human friendly name

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    # Override the __str method so the object in the ORM has a human friendly name

    def __str__(self):
        return self.name


class Record(models.Model):
    title = models.CharField(max_length=100)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    # why does null work in python?
    releaseDate = models.DateField(null=True)
    # Override the __str method so the object in the ORM has a human friendly name

    def __str__(self):
        return self.title


class Song(models.Model):
    trackNumber = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    length = models.DurationField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    # Override the __str method so the object in the ORM has a human friendly name

    def __str__(self):
        return self.title
