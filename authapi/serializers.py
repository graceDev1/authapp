from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer, UserCreateSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone']