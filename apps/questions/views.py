from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Question
from .serializers import (
    QuestionSerializer,
)


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get', 'put', 'post']
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "question",
    ]
