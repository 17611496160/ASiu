# -*- encoding: utf-8 -*-
'''
@File : length.py
@Time : 2020/03/08 19:39:56
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def getlength(m):
#type = None
    if isinstance(m,str):
        return len(m)
    elif isinstance(m,list):
        return len(m)
    elif isinstance(m,tuple):
        return len(m)


string = input("请输入一行字符串：")
temp = int(input("请输入一个类型(字符串：1、列表：2、元组：3)："))
if temp == 1:
    print("该字符串的长度为：",getlength(string))
if temp == 2:
    print("该列表的长度为：",getlength(list(string)))
    print(list(string))
if temp == 3:
    print("该元组的长度为：",getlength(tuple(string)))
    print(tuple(string))
