from django.db import models
from apps.attendance.models import Subject, Student
from apps.attendance.models import AttendanceReport, Satus, Subject


class DailyAttendanceStat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='daily_stats')
    subjects = models.ManyToManyField(Subject)
    day = models.DateField()

    class Meta:
        verbose_name = 'Daily Attendance Stat'
        verbose_name_plural = 'Daily Attendance Stats'
        ordering = ['-day']
    
    def run_report_and_save(self):
        query = AttendanceReport.objects.filter(attendance__date__day=18, attendance__date__month=11, attendance__date__year=2022, status=Satus.ABSENT)
        for i in query:
            if self.objects.filter(day=i.attendance.date, student=i.student).exists():
                a = self.objects.get(student=i.student, day=i.attendance.date)
                a.subjects.add(i.attendance.subject)
                a.save()
            else:
                x = self.objects.create(student = i.student, day = i.attendance.date)
                x.subjects.add(i.attendance.subject)
                x.save()