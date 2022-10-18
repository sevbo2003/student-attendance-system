from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import urls as rest_auth
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.authentication.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('rest-auth/', include(rest_auth)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)