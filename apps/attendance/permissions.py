from rest_framework.permissions import BasePermission
from apps.attendance.models import Attendance, Subject, Group
from apps.authentication.models import User


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_type == User.UserType.TEACHER:
                return True
            return False
        return False
    
    def has_object_permission(self, request, view, obj):

        if request.user.user_type == User.UserType.TEACHER:
            if isinstance(obj, Attendance):
                return obj.subject.teacher == request.user
            if isinstance(obj, Subject):
                return obj.teacher == request.user
            if isinstance(obj, Group):
                return obj.teacher == request.user
        return False