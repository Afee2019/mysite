# encoding: utf-8  


""" 
@author: 李绍俊
@license: Apache Licence  
@contact: 188792829@qq.com
@file: RandomName1.py 
@time: 2017/10/23 23:26 
"""

import random

a1 = ['赵','钱','孙','李','周','吴','郑','王','林','冯','陈','曹','杨','刘','朱','宋','杜','钟','梁','张','徐']
a2 = ['玉','明','龙','芳','军','玲','俊','杰','志','中','林','国','少','华','章','月','海','天','学','乐']
a3 = ['','立','玲','','国','康','海','','丽','','军','龙','英','华','明','','博','文','','娟']


def get_random_name():
    name = random.choice(a1)+random.choice(a2)+random.choice(a3)
    return name


# print(get_random_name())