from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import urls as rest_auth
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Student Attendance System API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('accounts/', include('apps.authentication.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('dailystat/', include('apps.dailystat.urls')),
    path('rest-auth/', include(rest_auth)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)