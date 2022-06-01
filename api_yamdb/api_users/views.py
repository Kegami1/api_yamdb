from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView, TokenObtainSlidingView

from .serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import viewsets, mixins

from users.models import User
from .serializers import UserSerializer
from .permissions import AdminOnly, UserOwner
from rest_framework.decorators import action

class MyTokenObtainPairView(TokenObtainPairView):
# class MyTokenObtainPairView(TokenObtainSlidingView):

    serializer_class = MyTokenObtainPairSerializer


class Signup():
    pass



class UserApiViewSet(viewsets.ModelViewSet):
# class UserApiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (AdminOnly,)
    lookup_field = 'username'


    @action(methods=['get', 'patch'], detail=False, url_path='me')
    def user_me(self, request):
        user = get_object_or_404(User, username=self.request.user)
        print(user)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data) 

    # def get_permissions(self):
    # # Если в GET-запросе требуется получить информацию об объекте
    #     if self.user_me:
    #     # Вернем обновленный перечень используемых пермишенов
    #         return (UserOwner(),)
    # # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
    #     return super().get_permissions() 