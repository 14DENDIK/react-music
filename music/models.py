from django.db import models
from authentication.models import User


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='playlists'
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.ImageField(blank=True, default='images/default_album.png')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='albums'
    )

    def __str__(self):
        return '%s - %s' % (self.title, self.artist)


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    file = models.FileField()
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='songs'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='songs'
    )

    def __str__(self):
        return '%s - %s' % (self.title, self.artist)


class PlaylistSongRelation(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class SongLikeRelation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_songs'
    )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='users_liked'
    )


class AlbumLikeRelation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='liked_albums'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='users_liked'
    )
