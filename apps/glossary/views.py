from datetime import date
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import Case, When, Value
from rest_framework import status as http_status, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from django_filters.rest_framework import DjangoFilterBackend

from apps.users.permissions import IsCardIssueManager, IsCardDeliveryManager, IsCardIssueManagerOrCardDeliveryManager
from apps.users import RoleTypes

from . import StatusTypes, CARD_ISSUE_MANAGER_STATUSES, CARD_DELIVERY_MANAGER_STATUSES
from .filters import CardApplicationListFilter
from .models import CardApplication
from .tasks import import_client_data_task
from .serializers import (
    CardApplicationSerializer,
    CardApplicationListSerializer,
    CardApplicationListExportSerializer,
    UploadCardApplicationFileSerializer,
    CardApplicationChangeStatusSerializer,
    CardApplicationIdListSerializer,
    CardApplicationsChangeListResponse,
    CardApplicationsSendToDeliveryListResponse, ReportFilterSerializer, CardApplicationReportExportSerializer
)
from .integrations.mykhat import MyKhatAPI



class CardApplicationViewSet(ModelViewSet):
    queryset = CardApplication.objects.all()
    serializer_class = CardApplicationSerializer
    http_method_names = ['get', 'put', 'post']
    permission_classes = [IsCardIssueManagerOrCardDeliveryManager]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        # status_order = [(choice[0], index) for (index, choice) in enumerate(StatusTypes.choices, start=1)]
        # print(status_order)
        # qs.order_by(
        #     Case(
        #         *[When(status=choice, then=Value(index)) for choice, index in status_order]
        #     )
        # )
        # if request.user.role == RoleTypes.card_issue_manager:
        #     self.queryset = self.queryset.filter(status__in=CARD_ISSUE_MANAGER_STATUSES)
        if self.request.user.role == RoleTypes.card_delivery_manager:
            queryset = self.queryset.filter(status__in=CARD_DELIVERY_MANAGER_STATUSES)
        if self.request.user.role == RoleTypes.freedom_account:
            queryset = CardApplication.objects.none()
        if self.request.user.role == RoleTypes.mykhat_account:
            queryset = CardApplication.objects.none()

        return queryset.order_by('-created_at')

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CardApplicationListFilter
    search_fields = [
        "personal_data__first_name",
        "personal_data__last_name",
        "personal_data__middle_name",
        "personal_data__mobile_phone",
        "personal_data__client_d_account",
    ]

    def get_serializer_class(self):
        if self.action == "list":
            return CardApplicationListSerializer

        return CardApplicationSerializer
