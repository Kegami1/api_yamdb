from django.urls import path, include
from rest_framework import routers 

from api.views import ReviewViewSet, CommentViewSet, CategoriesList, GenreList

router = routers.DefaultRouter()

router.register('categories', CategoriesList, basename='categories')
router.register('genres', GenreList, basename='genres')
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