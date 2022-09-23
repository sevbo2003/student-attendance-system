from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.authentication.managers import CustomUserManager

class UserType(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    TEACHER = 'teacher', 'Teacher'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username=None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    user_type = models.CharField(choices=UserType.choices, max_length=10, default=UserType.TEACHER)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
