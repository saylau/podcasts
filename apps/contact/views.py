from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .models import City
from .serializers import ContactCitySerializer
# Create your views here.

class ContactViewSet(ListAPIView):
    queryset = City.objects.all()
    serializer_class = ContactCitySerializer
    permission_classes = (AllowAny, )
    pagination_class = LimitOffsetPagination