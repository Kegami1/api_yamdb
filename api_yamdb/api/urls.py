from django.urls import path, include
from rest_framework import routers 

from api.views import ReviewList, ReviewDetail, CommentList, CommentDetail, CategoriesList, GenreList

router = routers.DefaultRouter()

router.register('categories', CategoriesList, basename='categories')
router.register('genres', GenreList, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/titles/<int:title_id>/reviews/', ReviewList.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/', ReviewDetail.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/comments/', CommentList.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/comments/<int:comment_id>/', CommentDetail.as_view()),
]