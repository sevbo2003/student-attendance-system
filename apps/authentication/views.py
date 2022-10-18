from django.contrib.auth import logout
from typing import List
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView 
from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    http_method_names: List[str] = ['get']

    def get_queryset(self):
        queryset = User.objects.all()
        user_type = self.request.query_params.get('user_type', None)  # type: ignore
        if user_type is not None:
            queryset = queryset.filter(user_type=user_type)
        return queryset


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"msg": "Successfully Logged out"}, status=status.HTTP_200_OK)