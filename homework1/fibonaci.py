# -*- encoding: utf-8 -*-
'''
@File : fibonaci.py
@Time : 2020/03/06 18:53:13
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 6  前面2个元素为0，1，输出100以内的斐波那契数列；
def fib(list,n):
    a,b = 0,1
    list.append(a)
    list.append(b)
    while a + b <= n:
        a,b = b,a + b
        list.append(b)
    

list1 = []
fib(list1,100)
print(list1)