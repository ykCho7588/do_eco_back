'''
#routers 관련 코드를 하위 url에 옮긴 것
from django.urls import path, include
from rest_framework import routers

from doeco_app.views import UserViewSet, PostViewSet, CommentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter() #users라는 url에 UserViewSet을 맵핑 
router.register(r'user', UserViewSet)#url에 직접 적용됨
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
'''

from doeco_app import views 
from django.urls import path
urlpatterns = [
    path('post/', views.PostListAPIView.as_view(), name='post-list'), #게시물 목록 보기
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'), #게시물 detail
    path('post/create/', views.PostCreateAPIView.as_view(), name='post-detail'), # 게시물 작성
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'), # 댓글 작성
    path('post/<int:pk>/comment/', views.PostCommentRetrieveAPIView.as_view(), name='post-commentlist'), # 게시물 댓글 확인 
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'), #게시물 좋아요 수 확인 => refresh마다 좋아요 수 +1
    path('comment/<int:pk>/like/', views.CommentLikeAPIView.as_view(), name='comment-like'),
]