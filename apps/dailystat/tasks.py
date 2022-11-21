from config.celery import app
from apps.dailystat.models import DailyAttendanceStat
from apps.attendance.models import Subject, Student
from apps.attendance.models import AttendanceReport, Satus, Subject
from datetime import datetime


@app.task
def send_daily_stats():
    query = AttendanceReport.objects.filter(attendance__date = datetime.today().date(), status=Satus.ABSENT)
    for i in query:
        if DailyAttendanceStat.objects.filter(day=i.attendance.date, student=i.student).exists():
            a = DailyAttendanceStat.objects.get(student=i.student, day=i.attendance.date)
            a.subjects.add(i.attendance.subject)
            a.save()
        else:
            x = DailyAttendanceStat.objects.create(student = i.student, day = i.attendance.date)
            x.subjects.add(i.attendance.subject)
            x.save()