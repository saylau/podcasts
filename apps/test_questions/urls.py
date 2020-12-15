from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    # TestViewSet,
    CategoryListView,
    TestListView,
    QuestionListView,
)

# router = DefaultRouter()
# router.register(r'tests', TestViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('categories/', CategoryListView.as_view()),
    path('<int:category_id>/', TestListView.as_view()),
    path('questions/<int:test_id>/', QuestionListView.as_view()),
]