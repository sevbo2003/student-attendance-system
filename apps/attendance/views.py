from typing import List
from rest_framework import viewsets, status, response
from rest_framework.decorators import action
from apps.attendance.serializers import StudentSerializer, GroupSerializer, SubjectSerializer, AttendanceSerializer, AttendanceReportSerializer, AttendanceReportViewSerializer
from apps.attendance.models import Student, Group, Subject, Attendance, AttendanceReport
from apps.attendance.permissions import IsTeacher
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    http_method_names: List[str] = ['get', 'head', 'options']
    
    @action(detail=True, methods=['get'])
    def attendances(self, request, pk=None):
        student = self.get_object()
        attendances = student.attendance_reports.all()
        status = request.query_params.get('status', None)
        if status is not None:
            attendances = attendances.filter(status=status)
        else:
            attendances = attendances.all()
        page = self.paginate_queryset(attendances)
        if page is not None:
            serializer = AttendanceReportViewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AttendanceReportViewSerializer(attendances, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    http_method_names: List[str] = ['get', 'head', 'options']
    
    @action(detail=True, methods=['get'])
    def students(self, request, pk):
        group = self.get_object()
        students = Student.objects.filter(group=group)
        page = self.paginate_queryset(students)
        if page is not None:
            serializer = StudentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = StudentSerializer(students, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def subjects(self, request, pk):
        group = self.get_object()
        subjects = Subject.objects.filter(group__name=group.name)
        page = self.paginate_queryset(subjects)
        if page is not None:
            serializer = SubjectSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = SubjectSerializer(subjects, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    http_method_names: List[str] = ['get', 'head', 'options']
    permission_classes = [IsAdminUser]


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all().order_by('-date')
    permission_classes = [IsAuthenticated]
    http_method_names: List[str] = ['get', 'head', 'options', 'post']

    @action(detail=True, methods=['get'])
    def reports(self, request, pk):
        attendance = self.get_object()
        guruh = request.GET.get('group')
        if guruh is not None:
            queryset = attendance.reports.filter(student__group__id=guruh)
        else:
            queryset = attendance.reports.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AttendanceReportSerializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AttendanceReportSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def date(self, request):
        day = request.GET.get('day')
        if day:
            day = day.split('-')
            attendance = Attendance.objects.filter(
                subject__teacher = request.user,
                date__year = int(day[0]),
                date__month = int(day[1]),
                date__day = int(day[2])
            )
            if attendance:
                return response.Response([{'subject_id': i.subject.id, 'attendance_id': i.id} for i in attendance])
            return response.Response({'detail': 'Attendance not found'})
        return response.Response({'detail': 'Attendance not found'})

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(subject_id=self.request.data['subject'])


class AttendanceReportViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceReportSerializer
    queryset = AttendanceReport.objects.all().order_by('-attendance__date')
    http_method_names: List[str] = ['get', 'put', 'patch', 'head', 'options', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(attendance_id=self.request.data['attendance'])