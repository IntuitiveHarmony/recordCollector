from django.contrib import admin
from .models import Record, Band, Song, Genre

# Register your models here.
admin.site.register(Record)
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(Genre)
