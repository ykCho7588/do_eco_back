from django.db import models

from django.contrib.auth.models import User 


# Create your models here.
# 자유게시판 모델 구현
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# 자유게시판 댓글 구현
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Ecospot(models.Model):
    name=models.CharField(max_length=15)
    location = models.CharField(max_length=50, default='')

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)