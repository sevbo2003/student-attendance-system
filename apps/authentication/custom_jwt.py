# Update jwt serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
from apps.authentication.validation import isValid
from apps.authentication.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()
        if isValid(email=email):
            if user:
                if user.check_password(password):
                    data = super().validate(attrs)
                    refresh = self.get_token(user)
                    data['access'] = str(refresh.access_token)
                    data['refresh'] = str(refresh)
                    user_info = {
                        'id': user.id,
                        'first_name': user.first_name,
                        'last_name': user.last_name
                    }
                    data['user'] = user_info
                    return data
                else:
                    raise ValidationError({'detail': 'Email or password is incorrect'})
            else:
                raise ValidationError({'detail': 'Email or password is incorrect'})
        else:
            raise ValidationError({'detail': 'Please enter a valid email address'})

    def get_token(self, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


# Update TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer