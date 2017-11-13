# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 14:51
# @Author  : 李绍俊
# @Email   : 188792829@qq.com
# @File    : urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]