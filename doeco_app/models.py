from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    post_writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    #tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50)
    #description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')
    image = models.ImageField('IMAGE', upload_to='media/doeco_app/%Y/%m/', blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    class Meta:
        ordering = ('update_dt',)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment_writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content

class Ecospot(models.Model):
    name=models.CharField(max_length=15)
    location = models.CharField(max_length=50, default='')

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)