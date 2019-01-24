"""delbug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from bug import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login_action/', views.login_action),  # 登录动作处理路由
    path('my_projects/', views.my_projects),  # 我的项目列表页路由
    path('accounts/login/', views.index),  # 登录
    path('search_name/', views.search_name),  # 项目列表页搜索路由
    path('search_bugs/', views.search_bugs),  # 项目详情页缺陷搜索路由
    path('my_teams/', views.my_teams),  # 我的团队列表页路由
    re_path('(?P<pid>[0-9]+)/create_bug/', views.create_bug),  # 新建缺陷页面路由
    path('create_action/', views.create_action),  # 新建缺陷提交动作处理
    re_path('project_details/(?P<pid>[0-9]+)/', views.project_details),  # 项目详情页路由
]
