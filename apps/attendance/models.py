from django.db import models
from apps.authentication.models import User
import csv
import json

class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def fetch_attendance(self):
        return Attendance.objects.filter(student=self)
    
    def load_students_from_csv(self, file):
        with open('student.csv', 'r') as f:
            reader = csv.reader(f).decode('utf-8')
            for row in reader:
                group = Group.objects.get_or_create(name=row[3])
                Student.objects.create(first_name=row[0], last_name=row[1], email=row[2], group=group)

    def load_students_from_json(self):
        with open('ajou.json', 'r') as f:
            for i in json.load(f):
                group = Group.objects.get(name=i['group'])
                Student.objects.create(first_name=i['full_name'].split()[1], last_name=i['full_name'].split()[0], email=(str(i['full_id'])+"@ajou.uz"), group=group)

    @property
    def get_attendances(self):
        return self.attendance_reports.all()
    
    @property
    def get_absents_and_lates(self):
        return self.attendance_reports.filter(models.Q(status='absent') | models.Q(status='late'))
    
    @property
    def get_subjects(self):
        return self.group.subjects.all()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['last_name', 'first_name']

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name + ' - ' + self.group.name
    

class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, related_name='subjects', on_delete=models.CASCADE)                
    group = models.ManyToManyField(Group, related_name='subjects')
    slug = models.SlugField(max_length=50)

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