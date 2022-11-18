from django_filters import rest_framework as filters
from apps.dailystat.models import DailyAttendanceStat
from apps.attendance.models import Subject, Student
from apps.attendance.models import AttendanceReport, Satus, Subject
from django.db.models import Q


class DailyAttendanceStatFilter(filters.FilterSet):
    student = filters.CharFilter(method='filter_student')
    subjects = filters.CharFilter(method='filter_subjects_by_slug')

    class Meta:
        model = DailyAttendanceStat
        fields = ['student', 'subjects']
    
    def filter_student(self, queryset, name, value):
        return queryset.filter(Q(student__first_name__icontains=value) | Q(student__last_name__icontains=value))
    
    def filter_subjects_by_slug(self, queryset, name, value):
        return queryset.filter(subjects__slug=value)