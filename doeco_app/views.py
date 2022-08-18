from calendar import c
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import OuterRef

from doeco_app.serializers import PostListSerializer, CommentSerializer, PostRetrieveSerializer, UserListSerializer
from doeco_app.models import Post, Comment

#seojin code
from django.shortcuts import render
import requests
import json
from .models import Ecospot

def main(request):
        return render(request, 'main.html')

def Ecospots(request):
        ecospots = Ecospot.objects.all
        return render(request, 'ecospot.html', {'ecospots':ecospots})

#yoonkyeong code
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

#POST
class PostListAPIView(ListAPIView): #게시물 보기(GET)
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView): #게시물 detail(GET)
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostRetrieveSerializer

class PostCreateAPIView(CreateAPIView): # 게시물 create(POST)
    queryset = Post.objects.all() #대상 table: Post
    serializer_class = PostRetrieveSerializer

class PostDeleteAPIView(DestroyAPIView): #게시물 삭제 (DELETE)
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

class PostUpdateAPIView(UpdateAPIView): #게시물 update(PUT)
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

#COMMENT
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all() #대상 table: Comment
    serializer_class = CommentSerializer

class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all() #대상 table: Comment
    serializer_class = CommentSerializer

class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all() #대상 table: Comment
    serializer_class = CommentSerializer

#POST COMMENT
class PostCommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        postId=  self.kwargs.get('pk')
        comment = Comment.objects.filter(post=postId)
        return comment

class CommentRetrieveAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, pk, format=None):
        comment = get_object_or_404(Comment, id=pk)
        #comment = Comment.objects.filter(post = pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

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
