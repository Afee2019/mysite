from django.shortcuts import render

from django.http import HttpResponse

import MySQLdb as con

from .RandomName1 import get_random_name

import random






# Create your views here.
def test_pa(request):
    pa1 = request.GET['a']
    pa2 = request.GET['b']

    return HttpResponse(str(int(pa1)+int(pa2)))


def add(request, a, b):
    return HttpResponse(str(a+b))


def emp_list(request):
    cnx = con.connect(host='localhost',
                      port=3306,
                      user='root',
                      passwd='supermap',
                      database='test03',
                      charset='utf8')

    cur = cnx.cursor()

    strSQL = 'select * from emp'

    cur.execute(strSQL)

    cur.close()
    cnx.close()

    # return HttpResponse(strHeader+strMid+strTail)
    return render(request, 'emp/list1.html', {'myemp': cur})


def insert(request):
    cnx = con.connect(host='localhost',
                      port=3306,
                      user='root',
                      passwd='supermap',
                      database='test03',
                      charset='utf8')

    cur = cnx.cursor()

    strSQL = 'select max(emp_no) from emp'

    cur.execute(strSQL)

    max_emp_no = 0
    for r in cur:
        max_emp_no = int(r[0])

    max_emp_no += 1

    strName = get_random_name()

    gender = random.choice(['男', '女'])

    strSQL = f"insert into emp (emp_no, name, gender) " \
             f"values({max_emp_no}, '{strName}', '{gender}')"

    cur.execute(strSQL)

    cnx.commit()

    strSQL = 'select * from emp'

    cur.execute(strSQL)

    cur.close()
    cnx.close()

    return render(request, 'emp/list1.html', {'myemp': cur})