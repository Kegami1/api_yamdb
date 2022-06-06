from django.urls import path, include
from rest_framework import routers 

from api.views import ReviewViewSet, CommentViewSet, CategoriesViewSet, GenreViewSet, TitleViewSet

router = routers.DefaultRouter()

router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewViewSet,
    basename='review'
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
]