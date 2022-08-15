from rest_framework import serializers
from django.contrib.auth.models import User
from doeco_app.models import Post, Comment

#출력 포맷 혹은 출력 내용에 대한 코드#

# Serializers define the API representation.

class UserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
'''
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #client에 보내줄 필드 
        #fields = ['user', 'id', 'title', 'content','image','like', 'category']
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
'''
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #client에 보내줄 필드 
        #fields = ['post_writer', 'title', 'create_dt','region']
        fields = ['post_writer', 'title', 'create_dt','like']
        #fields = '__all__'

class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #client에 보내줄 필드 
        #fields = ['post_writer', 'id', 'title', 'content','image','like', 'category']
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
'''
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['like']
'''