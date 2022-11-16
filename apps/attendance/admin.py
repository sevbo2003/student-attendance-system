from django.contrib import admin
from apps.attendance.models import *


admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(Group)
admin.site.register(Student)


class M2MInline(admin.TabularInline):
    model = Subject.group.through
    extra = 1


class SubjectAdmin(admin.ModelAdmin):
    inlines = [M2MInline]
    list_display = ['name', 'slug', 'teacher']
    list_filter = ['teacher']
    search_fields = ['name', 'slug', 'teacher__first_name', 'teacher__last_name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subject, SubjectAdmin)