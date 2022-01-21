from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_home, name="music_home"),
    path('songs/', views.songs_list, name="songs_list"),
    path('albums/', views.album_list, name="album_list"),
    path('album/<int:album_id>', views.album_details, name="album_details")
]
