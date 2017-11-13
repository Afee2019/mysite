from django.shortcuts import render

from django.http import HttpResponse

import MySQLdb as con



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

