from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView, TokenObtainSlidingView

from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import viewsets, mixins

from .models import User
from .serializers import UserSerializer
from .permissions import AdminOnly

class MyTokenObtainPairView(TokenObtainPairView):
# class MyTokenObtainPairView(TokenObtainSlidingView):

    serializer_class = MyTokenObtainPairSerializer


class Signup():
    pass


class DetailViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminOnly,)


class UserDetail(APIView):

    # queryset = User.objects.all()
    # serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        permission_classes = (AdminOnly,)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserDetailViewSet(DetailViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AdminOnly,)

    # def get(self, request, *args, **kwargs):
    #     username = self.kwargs.get('username')
    #     user = get_object_or_404(User, username=username)
    #     # permission_classes = (AdminOnly,)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    def get_queryset(self):
        username = self.kwargs.get('username')
        print(username, '!!!!!!!!!!!!!!!!!!!!!!!!')
        user = get_object_or_404(User, username=username)
        return user