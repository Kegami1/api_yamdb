from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets

from reviews.models import Review, Comment, Genre, Category, Title
from api.serializers import ReviewSerializer, CommentSerializer, CategorySerializer, GenreSerializer
from api.mixins import ListDeleteViewSet
from api.permissions import ReadOnly, AuthorAdminModerator


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


class CategoriesList(ListDeleteViewSet):
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAdminUser | ReadOnly,)
    serializer_class = CategorySerializer


class GenreList(ListDeleteViewSet):
    queryset = Genre.objects.all()
    permission_classes = (permissions.IsAdminUser | ReadOnly,)
    serializer_class = GenreSerializer