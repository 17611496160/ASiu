# -*- encoding: utf-8 -*-
'''
@File : random.py
@Time : 2020/03/06 18:22:21
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# # 5  使用random模块，生成随机数，来初始化一个列表，元组；
#      使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
import random


list = []
for i in range(1,11):
    list.append(random.randint(0,100))
print(list)
tup = tuple(list)
print(tup)