from rest_framework.permissions import BasePermission
from apps.attendance.models import Attendance, Subject, Group
from apps.authentication.models import User, UserType


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.user_type in [UserType.TEACHER, UserType.ADMIN]:
                if Subject.objects.get(id=obj.id).teacher == request.user:
                    return True
            return False
        return False