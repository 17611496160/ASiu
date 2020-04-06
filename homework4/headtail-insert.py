# -*- encoding: utf-8 -*-
'''
@File : headtail-insert.py
@Time : 2020/03/29 17:13:49
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''
# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#     提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
import time
from collections import deque

list = [1,2,3,4,5,6,7,8,9,10]
time_start = time.time()
list.insert(0,0)
list.append(11)
print(list)
time_end = time.time()
print("用列表自带函数函数实现头插和尾插的运行时间为：",time_end - time_start)
time.sleep(1)
q = deque([1,2,3,4,5,6,7,8,9,10])
time1_start = time.time()
q.appendleft(0)
q.append(11)
print(q)
time1_end = time.time()
print("用deque实现头插和尾插的运行时间为：",time1_end - time1_start)
print("两者运行时间之差为：",(time1_end - time1_start) - (time_end - time_start))
