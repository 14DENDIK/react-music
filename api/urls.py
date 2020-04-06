from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from authentication.views import UserListView
from music.views import (
    AlbumListView,
    AlbumDetailView,
    SongListView,
    SongDetailView,
)

app_name = 'api'

urlpatterns = [
    path('user/', UserListView.as_view(), name='user-list'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('album/', AlbumListView.as_view(), name='all-albums-list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),
    path('song/', SongListView.as_view(), name='all-songs-list'),
    path('song/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
