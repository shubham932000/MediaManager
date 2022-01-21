from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
	list_display = ['title', 'artist', 'genre', 'rating', 'song_count']
	list_filter = ["rating", "genre"]
	search_fields = ["title", "artist", "genre"]
	actions = ["duplicate"]

	def song_count(self, album):
		return album.song_set.count()

	def duplicate(self, request, queryset):
		for album in queryset:
			new_album = Album()
			new_album.title = album.title + " (Copy)"
			new_album.artist = album.artist
			new_album.genre = album.genre
			new_album.rating = album.rating
			new_album.save()


class SongAdmin(admin.ModelAdmin):
	list_display = ['name', 'album']
	search_fields = ['name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)

