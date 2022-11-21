from rest_framework import viewsets
from apps.dailystat.models import DailyAttendanceStat
from apps.dailystat.serializers import DailyAttendanceStatSerializer
from apps.dailystat.filters import DailyAttendanceStatFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime


class DailyAttendanceStatViewSet(viewsets.ModelViewSet):
    queryset = DailyAttendanceStat.objects.filter(day=datetime.today().date()).order_by('student__last_name')
    serializer_class = DailyAttendanceStatSerializer
    http_method_names = ['get', 'head', 'options']
    filterset_class = DailyAttendanceStatFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
            try:
                queryset = DailyAttendanceStat.objects.filter(day=datetime.today().date()).order_by('student__last_name')
            except:
                last_day = DailyAttendanceStat.objects.first().day
                queryset = DailyAttendanceStat.objects.filter(day=last_day).order_by('student__last_name')
            return queryset