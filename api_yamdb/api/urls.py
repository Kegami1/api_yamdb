from django.urls import path

from api.views import ReviewList, ReviewDetail, CommentList, CommentDetail

urlpatterns = [
    path('v1/titles/<int:title_id>/reviews/', ReviewList.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/', ReviewDetail.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/comments/', CommentList.as_view()),
    path('v1/titles/<int:title_id>/reviews/<int:review_id>/comments/<int:comment_id>/', CommentDetail.as_view()),
]