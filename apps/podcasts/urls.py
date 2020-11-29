from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PodcastsViewSet,
    PlaylistViewSet,
)

router = DefaultRouter()
router.register(r'podcasts', PodcastsViewSet)
router.register(r'playlists', PlaylistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]