from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import permissions

from reviews.models import Review, Comment, Genre, Category, Title
from api.serializers import ReviewSerializer, CommentSerializer, CategorySerializer, GenreSerializer
from api.mixins import ListDeleteViewSet
from api.permissions import ReadOnly


class ReviewList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewSerializer


class CommentList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer


class CategoriesList(ListDeleteViewSet):
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAdminUser | ReadOnly,)
    serializer_class = CategorySerializer


class GenreList(ListDeleteViewSet):
    queryset = Genre.objects.all()
    permission_classes = (permissions.IsAdminUser | ReadOnly,)
    serializer_class = GenreSerializer