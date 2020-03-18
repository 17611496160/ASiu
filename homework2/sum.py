# -*- encoding: utf-8 -*-
'''
@File : sum.py
@Time : 2020/03/08 20:06:26
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 2 编写一个函数,接收n个数字，求这些参数数字的和;
def sum1(x):
    sumnub = sum(x)
    return sumnub

temp = input("请输入一串数字，用空格隔开：")
listnum = list(temp.split(" "))
listnum1 = []
for i in listnum:
    listnum1.append(int(i))
print("和为：",sum1(listnum1))