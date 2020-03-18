# -*- encoding: utf-8 -*-
'''
@File : print-odds.py
@Time : 2020/03/08 20:41:25
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#    数字列表请用随机数函数生成;
import random
def judge(x):
    print("该列表中的奇数有：")
    for it in x:
        if it%2 != 0:
            print(it,end = ' ')

            
list = []
for i in range(1,11):
    list.append(random.randint(0,100))
print("生成的列表为：",list)
judge(list)