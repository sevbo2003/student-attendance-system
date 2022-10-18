from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.attendance.views import StudentViewSet, GroupViewSet


router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(router.urls)),
]