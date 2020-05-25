"""myjiapu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve

import xadmin

from apps.users.views import HomeView, LoginView, LogoutView, SignupView, SignupVerifyView
from myjiapu.settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView .as_view(), name="signup"),
    path('verify/', SignupVerifyView.as_view(), name="verify"),

    url(r'^history/', include(('apps.history.urls', "history"), namespace="history")),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),

    # django-auth 登录、注册、登出
    # url(r'^accounts/', include('allauth.urls')),

    # 配置上传文件的访问路径
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # path('admin/', admin.site.urls, name="admin"),

]
