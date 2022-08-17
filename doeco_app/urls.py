from doeco_app import views 
from django.urls import path
urlpatterns = [
    #게시물 CRUD URI
    path('post/', views.PostListAPIView.as_view(), name='post-list'), #게시물 목록 보기(get)
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'), #게시물 detail(get) 
    path('post/create/', views.PostCreateAPIView.as_view(), name='post-create'), # 게시물 작성(post)
    path('post/<int:pk>/delete', views.PostDeleteAPIView.as_view(), name='post-delete'), #게시물 삭제 (delete)
    path('post/<int:pk>/edit', views.PostUpdateAPIView.as_view(), name='post-edit'), #게시물 수정 (update)
    #댓글
    path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'), # 댓글 작성(post)
    path('post/<int:pk>/comment/', views.PostCommentListAPIView.as_view(), name='post-commentlist'), # 게시물 댓글 확인(get)
    
    path('comment/<int:pk>/', views.CommentRetrieveAPIView.as_view(), name='comment-detail'), #댓글 보기
    path('comment/<int:pk>/delete', views.CommentDeleteAPIView.as_view(), name='comment-delete'), # 댓글 삭제(delete)
    path('comment/<int:pk>/edit', views.CommentUpdateAPIView.as_view(), name='comment-edit'), #댓글 수정(update)
    #좋아요
    path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'), #게시물 좋아요 수 확인 => refresh마다 좋아요 수 +1
    path('comment/<int:pk>/like/', views.CommentLikeAPIView.as_view(), name='comment-like'),#댓글 좋아요 수 확인 => refresh마다 좋아요 수 +1
]