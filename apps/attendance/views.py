from typing import List
from rest_framework import viewsets, status, response
from rest_framework.decorators import action
from apps.attendance.serializers import StudentSerializer, GroupSerializer, SubjectSerializer, AttendanceSerializer
from apps.attendance.models import Student, Group, Subject, Attendance
from apps.attendance.permissions import IsTeacher
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        group_id = self.request.query_params.get('group')
        print(group_id)
        if group_id:
            queryset = queryset.filter(group__id=group_id)
        return queryset

    @action(methods=['get'], detail=False)
    def group(self, request):
        group_name = request.query_params.get('group_name')
        students = Student.objects.filter(group__name=group_name)
        serializer = StudentSerializer(students, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_permissions(self):
        if self.action == 'create':
            return super().get_permissions()
        return []



class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @action(detail=True, methods=['get'])
    def students(self, request, pk):
        group = self.get_object()
        students = Student.objects.filter(group=group)
        serializer = StudentSerializer(students, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk):
        group = self.get_object()
        subjects = Subject.objects.filter(group=group)
        serializer = SubjectSerializer(subjects, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all().order_by('-date')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(subject_id=self.request.data['subject'])