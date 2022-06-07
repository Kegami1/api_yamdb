from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from api.mixins import ListCreateDestroyUpdateViewset, ListDeleteViewSet
from api.permissions import AuthorAdminModerator, MeAdmin
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleGetSerializer, TitleSerializer)
from reviews.models import Category, Genre, Review, Title


class SlugFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.query_params:
            if 'genre' in request.query_params.keys():
                slug = request.query_params['genre']
                titles = Title.objects.filter(genre__slug=slug)
                return titles
            if 'category' in request.query_params.keys():
                slug = request.query_params['category']
                titles = Title.objects.filter(category__slug=slug)
                return titles
            if 'year' in request.query_params.keys():
                year = request.query_params['year']
                titles = Title.objects.filter(year=year)
                return titles
            if 'name' in request.query_params.keys():
                name = request.query_params['name']
                titles = Title.objects.filter(name__contains=name)
                return titles
        return Title.objects.all()


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          AuthorAdminModerator)
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          AuthorAdminModerator)
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
    permission_classes = (MeAdmin,)
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListDeleteViewSet):
    queryset = Genre.objects.all()
    permission_classes = (MeAdmin,)

    serializer_class = GenreSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'slug')
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(ListCreateDestroyUpdateViewset):
    queryset = Title.objects.all()
    permission_classes = (MeAdmin,)
    serializer_class = TitleSerializer
    filter_backends = (SlugFilterBackend,)
    search_fields = ('id',)
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleGetSerializer
        return TitleSerializer
