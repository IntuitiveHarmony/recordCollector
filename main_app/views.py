from django.shortcuts import render
from .models import Record

# records = [
#     {'title': 'Cannity', 'artist': 'Jasper Cannity', 'release_year': 1983, 'image': 'https://cdn.midjourney.com/ea3b6ac2-ec61-4b15-9623-51030613dadd/0_3.png', 'track_list': ['Singin\' to the wind', 'Mary-Belle', 'The River Knows', 'Goin\' Downtown', 'Fields of Gold', 'Can\'t go on']},
#     {'title': 'Folk', 'artist': 'Sheppard Family Singers', 'release_year': 1958, 'image': 'https://cdn.midjourney.com/e1e9c890-c8f2-4a95-bb68-57dc9b7b6d0b/0_3.png', 'track_list': ['Mountain Man', 'Wanderlust', 'Winter\'s Chill', 'Homecoming', 'Fiddler\'s Green', 'Heartland']}
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {
        'records': records
    })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    # get a list of all the songs in the record and sort by the track number
    songs = record.song_set.all().order_by('trackNumber')
    # get the genres associated with the record
    genres = record.genre.all()
    print(genres)
    # render the record detail page and pass the record and songs in as context
    return render(request, 'records/detail.html', {'record' : record, 'songs' : songs, 'genres': genres})

# def song_detail(request, song_id):
#     song = Song.objects.get(id=song_id)
#     return render

