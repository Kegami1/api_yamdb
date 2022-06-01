from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSlidingSerializer
from rest_framework import serializers

from .models import User

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
        fields = '__all__'