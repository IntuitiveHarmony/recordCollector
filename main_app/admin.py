from django.contrib import admin
from .models import Record, Band, Song, Genre, Artist, Instrument

# Register your models here.
admin.site.register(Record)
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Instrument)
