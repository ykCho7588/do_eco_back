'''
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from doeco_app.serializers import UserSerializer, PostSerializer, CommentSerializer
from doeco_app.models import Post, Comment
#Create your views here.

#ModelViewSet 상속 받음
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() #대상 table: User
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() #대상 table: Comment
    serializer_class = CommentSerializer
'''
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.response import Response

from doeco_app.serializers import PostListSerializer, CommentSerializer, PostRetrieveSerializer, UserListSerializer
from doeco_app.models import Post, Comment

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostRetrieveSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostRetrieveSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all() #대상 table: Comment
    serializer_class = CommentSerializer

class PostCommentRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    
'''
class PostLikeAPIView(UpdateAPIView):
    queryset = Post.objects.all() #대상 table: Comment
    serializer_class = PostLikeSerializer
    # PATCH method
    #like 갯수를 증가시키고 update하는 코드 
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = {'like': instance.like + 1}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        #like 숫자로 보내기
        return Response(data['like'])
'''
class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all() #대상 table: Comment

    #GET 메소드를 통해 refresh할때마다 좋아요 수가 증가함
    def get(self, request, *args, **kwargs):
        #partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.like += 1
        instance.save()
        #data = {'like': instance.like + 1}
        
        #like 숫자로 보내기
        return Response(instance.like)

class CommentLikeAPIView(GenericAPIView):
    queryset = Comment.objects.all() #대상 table: Comment
    
    #GET 메소드를 통해 refresh할때마다 좋아요 수가 증가함
    def get(self, request, *args, **kwargs):
        #partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.like += 1
        instance.save()
        #data = {'like': instance.like + 1}
        
        #like 숫자로 보내기
        return Response(instance.like)
