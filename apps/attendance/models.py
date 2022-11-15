from django.db import models
from apps.authentication.models import User


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name + ' - ' + self.group.name
    

class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, related_name='subjects', on_delete=models.CASCADE)
    group = models.ManyToManyField(Group, related_name='subjects')

    def __str__(self) -> str:
        return self.name


class Satus(models.TextChoices):
    PRESENT = 'present', 'Present'
    ABSENT = 'absent', 'Absent'
    LATE = 'late', 'Late'


class Attendance(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject.name + ' - ' + self.date.strftime('%d-%m-%Y')

    class Meta:
        ordering = ['-date']
    

class AttendanceReport(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='reports')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_reports')
    status = models.CharField(choices=Satus.choices, max_length=10, default=Satus.ABSENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['student__last_name', 'student__first_name']

    def __str__(self) -> str:
        return self.student.first_name + ' ' + self.student.last_name + ' - ' + self.status + ' - ' + self.attendance.subject.name + ' - ' + self.attendance.date.strftime('%d-%m-%Y')