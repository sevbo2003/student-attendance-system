from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.dailystat.views import DailyAttendanceStatViewSet

router = DefaultRouter()
router.register('', DailyAttendanceStatViewSet, basename='dailystat')

urlpatterns = [
    path('', include(router.urls)),
]