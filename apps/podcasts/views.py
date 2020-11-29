from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import AudioRecord, Playlist
from .serializers import (
    AudioRecordSerializer,
    PlaylistSerializer
)


class PodcastsViewSet(ModelViewSet):
    queryset = AudioRecord.objects.all()
    serializer_class = AudioRecordSerializer
    http_method_names = ['get']
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "title",
    ]


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get']
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "title",
    ]
