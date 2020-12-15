from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import User, City
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer, ContactCitySerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class ContactViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = ContactCitySerializer
    http_method_names = ['get']
    pagination_class = LimitOffsetPagination
