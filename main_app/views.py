from django.shortcuts import render

records = [
    {'title': 'Cannity', 'artist': 'Jasper Cannity', 'release_year': 1983, 'image': 'https://cdn.midjourney.com/ea3b6ac2-ec61-4b15-9623-51030613dadd/0_3.png', 'track_list': ['Singin\' to the wind', 'Mary-Belle', 'The River Knows', 'Goin\' Downtown', 'Fields of Gold', 'Can\'t go on']},
    {'title': 'Folk', 'artist': 'Sheppard Family Singers', 'release_year': 1958, 'image': 'https://cdn.midjourney.com/e1e9c890-c8f2-4a95-bb68-57dc9b7b6d0b/0_3.png', 'track_list': ['Mountain Man', 'Wanderlust', 'Winter\'s Chill', 'Homecoming', 'Fiddler\'s Green', 'Heartland']}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def records_index(request):
    return render(request, 'records/index.html', {
        'records': records
    })