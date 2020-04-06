from django.contrib import admin

from .models import (
    Playlist,
    Song,
    Album,
    PlaylistSongRelation,
    SongLikeRelation,
    AlbumLikeRelation,
)

admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(PlaylistSongRelation)
admin.site.register(SongLikeRelation)
admin.site.register(AlbumLikeRelation)
