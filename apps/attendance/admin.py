from django.contrib import admin
from apps.attendance.models import *


admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Subject)
