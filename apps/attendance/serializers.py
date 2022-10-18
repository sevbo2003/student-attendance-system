from lib2to3.pgen2 import grammar
from rest_framework import serializers
from apps.attendance.models import Group, Subject, Student, Attendance, AttendanceReport, Satus


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)
    class Meta:
        model = Subject
        fields = '__all__'


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