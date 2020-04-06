from rest_framework import serializers
from .models import User
from music.models import SongLikeRelation, AlbumLikeRelation


class UserSerializer(serializers.ModelSerializer):
    liked_songs = serializers.PrimaryKeyRelatedField(many=True, queryset=SongLikeRelation.objects.all())
    liked_albums = serializers.PrimaryKeyRelatedField(many=True, queryset=AlbumLikeRelation.objects.all())

    class Meta:
        model = User
        fields = '__all__'
