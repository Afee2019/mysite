# -*- coding: utf-8 -*-
# @Time    : 2017/11/7 21:27
# @Author  : 李绍俊
# @File    : trans.py

f = open('list.html','r')
g = open('list1.html', 'w')

for l in f:
    if l.find('"../assets/') > -1:
        a = l.split('../assets/')

        b = a[1].replace('"', '\' %}"', 1)
        c = a[0] + '{% static \'/assets/' +b

        g.write(c)
    else:
        g.write(l)

f.close()
g.close()