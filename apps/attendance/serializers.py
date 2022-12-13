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
        fields =['id', 'name','teacher', 'group', 'slug']
    
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
    
    def create(self, validated_data):
        subject_id = validated_data['subject_id']
        date = validated_data['date']
        if not Subject.objects.filter(id=subject_id).exists():
            raise serializers.ValidationError("Subject doesn't exist")
        if Attendance.objects.filter(subject_id=subject_id, date=date).exists():
            raise serializers.ValidationError("Attendance date already exists")
        if Subject.objects.get(id=subject_id).teacher != self.context['request'].user:
            raise serializers.ValidationError("You are not the teacher of this subject")
        attendance = Attendance.objects.create(**validated_data)
        return attendance


class AttendanceReportSerializer(serializers.ModelSerializer):
    attendance = serializers.SerializerMethodField()
    
    class Meta:
        model = AttendanceReport
        fields = ['id', 'attendance', 'student', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_attendance(self, obj):
        attendance = {}
        attendance['id'] = obj.attendance.id
        attendance['date'] = obj.attendance.date
        attendance['subject'] = {
            'id': obj.attendance.subject.id,
            'name': obj.attendance.subject.name
        }
        return attendance
    
    def create(self, validated_data):
        attendance_id = validated_data['attendance_id']
        student = validated_data['student']
        if not Attendance.objects.filter(id=attendance_id).exists():
            raise serializers.ValidationError("Attendance doesn't exist")
        if not Student.objects.filter(id=student.id).exists():
            raise serializers.ValidationError("Student doesn't exist")
        if AttendanceReport.objects.filter(attendance_id=attendance_id, student_id=student.id).exists():
            raise serializers.ValidationError("Attendance already taken")
        if Attendance.objects.get(id=attendance_id).subject.teacher != self.context['request'].user:
            raise serializers.ValidationError("You are not the teacher of this subject")
        x = Attendance.objects.get(id=attendance_id).subject.group.all()
        if student.group not in x:
            raise serializers.ValidationError("Student doesn't belong to this group")
        attendance_report = AttendanceReport.objects.create(**validated_data)
        return attendance_report
    
    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class AttendanceReportViewSerializer(serializers.ModelSerializer):
    attendance = serializers.SerializerMethodField()
    student = StudentSerializer()
    
    class Meta:
        model = AttendanceReport
        fields = ['id', 'attendance', 'student', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_attendance(self, obj):
        attendance = {}
        attendance['id'] = obj.attendance.id
        attendance['date'] = obj.attendance.date
        attendance['subject'] = {
            'id': obj.attendance.subject.id,
            'name': obj.attendance.subject.name
        }
        return attendance