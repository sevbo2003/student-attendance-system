from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.attendance.views import StudentViewSet, GroupViewSet, SubjectViewSet, AttendanceViewSet, AttendanceReportViewSet


router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('groups', GroupViewSet, basename='groups')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('attendances', AttendanceViewSet, basename='attendances')
router.register('attendance-report', AttendanceReportViewSet, basename='attendance-reports')


urlpatterns = [
    path('', include(router.urls)),
]