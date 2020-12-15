from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .users.views import UserViewSet, UserCreateViewSet
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

internal_schema_view = get_schema_view(
    openapi.Info(
        title="Podcasts API", default_version="v1", description="Podcasts",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # urlconf="apps.urls"
)

schema_view = get_schema_view(
    openapi.Info(
        title="Podcasts API", default_version="v1", description="Podcasts",
    ),
    public=False,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/contacts/', include('apps.contact.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('devices/', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('', include('apps.glossary.urls')),
    path('', include('apps.podcasts.urls')),
    path('', include('apps.questions.urls')),
    path('', include('apps.test_questions.urls')),
    path(
        "api/docs/internal/",
        internal_schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
