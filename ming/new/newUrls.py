# -*- coding: utf-8 -*-
# @Time     : 2023/11/9 20:48
# @Author   : JiMing
# @File     : newUrls.py
# @SoftWare : PyCharm
from django.urls import path
from .views import index, newList, newListTemplate

# 配置路由规则
urlpatterns = [
    path('index/', index),
    # 新闻列表
    path('newList/', newList),
    path('newList1/', newListTemplate),
]
