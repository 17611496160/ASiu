# -*- encoding: utf-8 -*-
'''
@File : find-similar.py
@Time : 2020/03/06 16:37:59
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
list1 = [1,3,5,2,7,9,5]
list2 = [2,4,6,8,10,1,9]
print("两列表相同的元素有：",end = '')
for i in list1:
    if i in list2:
        print(i,end = ' ')
