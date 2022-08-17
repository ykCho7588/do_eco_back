from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

urlpatterns = [
    #admin 사이트 연결
    path('admin/', admin.site.urls),

    path('doeco_app/', include('doeco_app.urls')),
    #path('', include(router.urls)),
    #화면에 로그인 기능을 보여주는 역할 (Log in)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

