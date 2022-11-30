from typing import List
from rest_framework.viewsets import ModelViewSet
from apps.authentication.models import User,UserType
from apps.attendance.permissions import IsTeacher
from apps.authentication.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.attendance.serializers import GroupSerializer, SubjectSerializer
from rest_framework.decorators import action


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    http_method_names: List[str] = ['get', 'head', 'options']

    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        user = self.get_object()
        subjects = user.subjects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        if self.action == 'subjects':
            self.permission_classes = [IsAuthenticated, IsTeacher]
        return super().get_permissions()


class TeacherViewSet(ModelViewSet):
    queryset = User.objects.filter(user_type=UserType.TEACHER)
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    http_method_names: List[str] = ['get','post', 'head', 'options']

    def create(self, request, *args, **kwargs):
        if self.action == 'update_password':
            return super().create(request, *args, **kwargs)
        return Response({"detail": "You do not have permission to do this  operations"})

    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        user = self.get_object()
        subjects = user.subjects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'])
    def update_password(self, request):
        if request.user.is_authenticated:
            user = request.user
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if new_password != confirm_password:
                return Response({'detail': 'Password does not match.'}, status=status.HTTP_400_BAD_REQUEST)
            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password successfully updated"}, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.action in ['update_password', 'me']:
            self.permission_classes = [IsTeacher]
        return super().get_permissions()
    