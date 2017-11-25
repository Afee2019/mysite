from django.shortcuts import render

from django.http import HttpResponse

import MySQLdb as con

from .RandomName1 import get_random_name

import random

from .models import Emp, Dept





# Create your views here.
def test_pa(request):
    pa1 = request.GET['a']
    pa2 = request.GET['b']

    return HttpResponse(str(int(pa1)+int(pa2)))


def add(request, a, b):
    return HttpResponse(str(a+b))


# def emp_list(request):
#     cnx = con.connect(host='localhost',
#                       port=3306,
#                       user='root',
#                       passwd='supermap',
#                       database='test03',
#                       charset='utf8')
#
#     cur = cnx.cursor()
#
#     strSQL = 'select * from emp'
#
#     cur.execute(strSQL)
#
#     cur.close()
#     cnx.close()
#
#     # return HttpResponse(strHeader+strMid+strTail)
#     return render(request, 'emp/list1.html', {'myemp': cur})

def emp_list(request):
    return render(request,  'emp/list1.html', {'myemp': Emp.objects.all()})


# def insert(request):
#     1. 得到最大的emp_no, +1
#     2. 生成随机的姓名
#     3. 性别随机生成
#     4. email处理生成
#     5. Emp .save()
#
#     cnx = con.connect(host='localhost',
#                       port=3306,
#                       user='root',
#                       passwd='supermap',
#                       database='test03',
#                       charset='utf8')
#
#     cur = cnx.cursor()
#
#     strSQL = 'select max(emp_no) from emp'
#
#     cur.execute(strSQL)
#
#     max_emp_no = 0
#     for r in cur:
#         max_emp_no = int(r[0])
#
#     max_emp_no += 1
#
#     strName = get_random_name()
#
#     gender = random.choice(['男', '女'])
#
#     strSQL = f"insert into emp (emp_no, name, gender) " \
#              f"values({max_emp_no}, '{strName}', '{gender}')"
#
#     cur.execute(strSQL)
#
#     cnx.commit()
#
#     strSQL = 'select * from emp'
#
#     cur.execute(strSQL)
#
#     cur.close()
#     cnx.close()
#
#     return render(request, 'emp/list1.html', {'myemp': cur})

def insert(request):
    new_emp_no = Emp.objects.all().order_by('-emp_no')[0].emp_no + 1
    strName = get_random_name()
    gender = random.choice(['男', '女'])
    d = Dept.objects.all()[0]
    email = 'abc@supermap.com'

    a = Emp(emp_no=new_emp_no, name=strName, gender=gender, dept=d, email=email)

    a.save()

    return render(request, 'emp/list1.html', {'myemp': Emp.objects.all()})

