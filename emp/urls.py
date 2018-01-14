# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 21:57
# @Author  : 李绍俊
# @Email   : 188792829@qq.com
# @File    : urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('test_pa/', views.test_pa, name='test_pa'),
    path('add/<int:a>/<int:b>/', views.add, name='add'),


    path('list/', views.emp_list, name='list'),
    # path('insert/', views.insert, name='insert'),
]