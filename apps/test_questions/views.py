from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Test, Category, TestQuestion
from .serializers import (
    TestSerializer,
    CategorySerializer,
    TestQuestionSerializer,
)

class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination


class TestListView(ListAPIView):
    serializer_class = TestSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Test.objects.filter(category_id=self.kwargs['category_id'])

    def get(self, requets, category_id):
        return super().get(request, category_id)

class QuestionListView(ListAPIView):
    serializer_class = TestQuestionSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return TestQuestion.objects.filter(test_id=self.kwargs['test_id'])

    def get(self, requets, test_id):
        return super().get(request, test_id)

# class TestViewSet(ModelViewSet):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer
#     http_method_names = ['get']
#     pagination_class = LimitOffsetPagination

#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     search_fields = [
#         "title",
#     ]
