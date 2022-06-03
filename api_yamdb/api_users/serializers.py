from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSlidingSerializer
from rest_framework import serializers

from users.models import User
from django.contrib.auth.hashers import make_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
# class MyTokenObtainPairSerializer(TokenObtainSlidingSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        # token['name'] = user.name
        # ...


        return token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')

    # def validate_password(self, value: str) -> str:
    #     password = make_password(value)
    #     print(password)
    #     return make_password(value)