from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets

from reviews.models import Review, Comment, Genre, Category, Title
from api.serializers import ReviewSerializer, CommentSerializer, CategorySerializer, GenreSerializer, TitleSerializer
from api.mixins import ListDeleteViewSet, ListCreateDestroyUpdateViewset
from api.permissions import ReadOnly, MeAdmin
from api.permissions import ReadOnly, AuthorAdminModerator

from rest_framework.permissions import AllowAny


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AuthorAdminModerator)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        queryset = title.reviews.order_by('id')
        return queryset

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, AuthorAdminModerator)    
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        queryset = review.comments.order_by('id')
        return queryset

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        serializer.save(
            author=self.request.user,
            review=review
        )


class CategoriesViewSet(ListDeleteViewSet):
    queryset = Category.objects.all()
    permission_classes = (MeAdmin | ReadOnly,)
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListDeleteViewSet):
    queryset = Genre.objects.all()
    permission_classes = (MeAdmin | ReadOnly,)
    serializer_class = GenreSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(ListCreateDestroyUpdateViewset):
    queryset = Title.objects.all()
    permission_classes = (MeAdmin | ReadOnly,)
    # permission_classes = (AllowAny,)

    serializer_class = TitleSerializer
    lookup_field = 'id'

    # def perform_create(self, serializer):
    #     if (self.request.data.get('genre') in Genre.objects.all()) and (
    #             self.request.data.get('category') in Category.objects.all()):
    #         genre = get_object_or_404(Genre, slug=self.request.data.get('genre'))
    #         category = get_object_or_404(Category, slug=self.request.data.get('category'))
    #         serializer.save(genre=genre, category=category)