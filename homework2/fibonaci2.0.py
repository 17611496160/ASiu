# -*- encoding: utf-8 -*-
'''
@File : fibonaci2.0.py
@Time : 2020/03/08 21:59:46
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 6  定义一个函数, 打印输出n以内的斐波那契数列;
def fib(list,n):
    a,b = 0,1
    list.append(a)
    list.append(b)
    while a + b <= n:
        a,b = b,a + b
        list.append(b)
    

list1 = []
n = int(input("请输入一个数字："))
fib(list1,n)
print(list1)