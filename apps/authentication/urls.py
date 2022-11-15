from django.urls import path, include
from apps.authentication.views import RegisterView, LogoutView, UserViewSet, TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('teachers', TeacherViewSet, basename='teachers')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
]