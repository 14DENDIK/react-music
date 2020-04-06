from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .permissions import IsOwnerOrReadOnly
from .models import Album, Song
from .serializers import (
    AlbumSerializer,
    SongSerializer,
    PlaylistSerializer,
    PlaylistSongRelationSerializer,
)


class AlbumListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = AlbumSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request,  pk, format=None):
        album = get_object_or_404(Album, pk=pk)
        songs = album.songs.all()
        album_ser = AlbumSerializer(album, many=False)
        songs_ser = SongSerializer(songs, many=True)
        return Response({
            'album': album_ser.data,
            'songs': songs_ser.data,
        })

    def put(self, request, pk, format=None):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        album = get_object_or_404(Album, pk=pk)
        album.detele()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = SongSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request,  pk, format=None):
        song = get_object_or_404(Album, pk=pk)
        song_ser = SongSerializer(song, many=False)
        return Response(song_ser.data)

    def put(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        song = get_object_or_404(Song, pk=pk)
        song.detele()
        return Response(status=status.HTTP_204_NO_CONTENT)
