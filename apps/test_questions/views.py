from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Test
from .serializers import (
    TestSerializer,
)


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    http_method_names = ['get']
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "title",
    ]
