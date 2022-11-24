from django.urls import path, include
from apps.authentication.views import UserViewSet, TeacherViewSet, DashboardCheckView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('teachers', TeacherViewSet, basename='teachers')


urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardCheckView.as_view(), name='dashboard'),
]