from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Song, Album


# Create your views here.
def music_home(request):
	return HttpResponse("<h1>It works !</h1>")


def songs_list(request):
	song_list = Song.objects.all()
	return render(request, "Music/song_list.html", context={"all_songs": song_list})


def album_details(request, album_id):
	album = get_object_or_404(Album, id=album_id)
	songs_list = Song.objects.filter(album=album)
	return render(request, "Music/album_details.html", context={"album": album, "songs": songs_list})

def album_list(request):
	album_list = Album.objects.all()
	return  render(request, "Music/album_list.html", context={"all_albums": album_list})
