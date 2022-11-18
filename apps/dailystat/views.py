from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from apps.dailystat.models import DailyAttendanceStat
from apps.dailystat.serializers import DailyAttendanceStatSerializer
import datetime


class DailyAttendanceStatViewSet(viewsets.ModelViewSet):
    queryset = DailyAttendanceStat.objects.filter(day=datetime.date.today()).order_by('student__last_name')
    serializer_class = DailyAttendanceStatSerializer
    http_method_names = ['get', 'head', 'options']
