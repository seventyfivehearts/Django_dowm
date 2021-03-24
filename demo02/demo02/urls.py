
"""demo02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 前后端传输数据的编码格式
    url(r'^index/', views.index),
    # ajax发送json格式数据
    url(r'^ab_json/', views.ab_json),
    # ajax 发送文件对象
    url(r'^ab_file/', views.ab_file),
    # 序列化相关
    url(r'^ab_ser/', views.ab_ser),

    # 用户展示界面
    url(r'^user/list/', views.user_list),
    url(r'^delete/user/', views.delete_user),
    # 批量插入数据
    url(r'^ab_pl/', views.ab_pl),
]
