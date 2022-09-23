from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from apps.authentication.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    
    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except:
            return None