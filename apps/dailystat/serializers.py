from rest_framework import serializers
from apps.dailystat.models import DailyAttendanceStat


class DailyAttendanceStatSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    
    class Meta:
        model = DailyAttendanceStat
        fields = '__all__'
    
    def get_student(self, obj):
        return {
            "id": obj.student.id,
            "first_name": obj.student.first_name,
            "last_name": obj.student.last_name,
        }
    
    def get_subjects(self, obj):
        return [
            {
                "id": i.id,
                "name": i.name.split('(')[0].rstrip(),
            }
            for i in obj.subjects.all()
        ]