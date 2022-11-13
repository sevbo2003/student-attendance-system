from rest_framework import serializers
from apps.attendance.models import Group, Subject, Student, Attendance, AttendanceReport, Satus


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)
    teacher = serializers.SerializerMethodField()
    class Meta:
        model = Subject
        fields =['id', 'name','teacher', 'group']
    
    def get_teacher(self, obj):
        teachers = []
        for teacher in obj.teacher.all():
            t = {}
            t['id'] = teacher.id
            t['name'] = teacher.first_name + teacher.last_name
            t['email'] = teacher.email
            teachers.append(t)
        return teachers   
    


class StudentSerializer(serializers.ModelSerializer):

    group = GroupSerializer()
    class Meta:
        model = Student
        fields = '__all__'
    
    def create(self, validated_data):
        group = validated_data.pop('group')
        group = Group.objects.get(id=group['name'])
        student = Student.objects.create(group=group, **validated_data)
        return student


class AttendanceSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    class Meta:
        model = Attendance
        fields = ['id', 'subject', 'date', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_subject(self, obj):
        subject = {}
        subject['id'] = obj.subject.id
        subject['name'] = obj.subject.name
        return subject
