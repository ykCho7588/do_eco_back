"""doecoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from doeco_app import views
from accounts import views as accounts_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main),
    path('admin/', admin.site.urls),
    path('place/', views.Ecospots),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout),
    path('register/', accounts_views.signup, name='register'),
    path('freehome/', views.freehome, name='freehome'),
    path('freepostcreate/', views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', views.freedetail, name='freedetail'),
    # 127.0.0.1:8000/detail/
    path('new_freecomment/<int:post_id>', views.new_freecomment, name='new_freecomment'),
    path('mypage/', views.Mypage, name="mypage"),
    path('ecorank/', views.ecorank, name="ecorank"),
    path('ecotip/', views.ecotip, name="ecotip"),
    path('zeroshop/', views.zeroshop, name="zeroshop"),
    path('ecospot/', views.ecospot, name="ecospot")
]
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)