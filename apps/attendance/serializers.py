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
        return {
            "id": obj.teacher.id,
            "name": obj.teacher.first_name + " " + obj.teacher.last_name
        } 
    


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
