from django.contrib import admin
from apps.dailystat.models import DailyAttendanceStat


@admin.register(DailyAttendanceStat)
class DailyAttendanceStatAdmin(admin.ModelAdmin):
    list_display = ('student', 'day')
    list_filter = ('day',)
    search_fields = ('student__first_name', 'student__last_name', 'day')