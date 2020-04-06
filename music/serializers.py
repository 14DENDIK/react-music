from rest_framework import serializers
from .models import (
    Album,
    Song,
    Playlist,
    PlaylistSongRelation,
)


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, queryset=Song.objects.all())
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    album = AlbumSerializer(many=False)

    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistSongRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlaylistSongRelation
        fields = '__all__'
