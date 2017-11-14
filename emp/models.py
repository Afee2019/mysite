# encoding: utf-8

from django.db import models

# Create your models here.


class Dept(models.Model):
    dept_no = models.IntegerField(verbose_name='部门编号')
    name = models.CharField(max_length=50, verbose_name='部门名称')


class Emp(models.Model):
    emp_no = models.IntegerField(verbose_name='工号')
    name = models.CharField(max_length=10, verbose_name='姓名')
    gender = models.CharField(max_length=2, verbose_name='性别')
    dept = models.ForeignKey(Dept,verbose_name='部门', on_delete=models.CASCADE)

