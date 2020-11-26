from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CardApplicationViewSet,
    CardApplicationListExportView,
    UploadCardApplicationFileView,
    ChangeStatusCardApplicationsView,
    SendToDeliveyCardApplicationsView,
    ApproveCardApplicationKYCView,
    RejectsCardApplicationKYCView,
    CardApplicationReportView,
    # UploadTradernetClientDataBaseFileView,
)

router = DefaultRouter()
router.register(r'cards', CardApplicationViewSet)

urlpatterns = [
    path("export/", CardApplicationListExportView.as_view()),
    path("import/", UploadCardApplicationFileView.as_view()),
    # path("import-client-base/", UploadTradernetClientDataBaseFileView.as_view()),
    path("change-status/", ChangeStatusCardApplicationsView.as_view()),
    path("send-to-delivery/", SendToDeliveyCardApplicationsView.as_view()),
    path("approve-kyc/<int:pk>/", ApproveCardApplicationKYCView.as_view()),
    path("reject-kyc/<int:pk>/", RejectsCardApplicationKYCView.as_view()),
    path("export-report/", CardApplicationReportView.as_view()),
    path('', include(router.urls)),
]