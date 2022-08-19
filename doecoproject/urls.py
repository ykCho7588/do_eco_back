from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from doeco_app import views
from accounts import views as accounts_views

urlpatterns = [
    path('doeco_app/', include('doeco_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', views.main),
    path('admin/', admin.site.urls),
    path('place/', views.Ecospots),
    path('login/', accounts_views.login),
    path('logout/', accounts_views.logout)]

#media file url
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)