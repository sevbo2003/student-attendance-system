from django.contrib import admin
from apps.authentication.models import User
from apps.authentication.forms import UserForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('user_type', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()
    list_per_page = 25
    form = UserForm