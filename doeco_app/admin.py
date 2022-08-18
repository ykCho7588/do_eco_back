from django.contrib import admin

from .models import Category, Comment, Post

from .models import Ecospot
# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)

admin.site.register(Ecospot)

