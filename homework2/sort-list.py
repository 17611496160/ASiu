# -*- encoding: utf-8 -*-
'''
@File : sort-list.py
@Time : 2020/03/09 16:30:46
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
def sortarray(array):
    array.sort()
    return array


inp = input("请输入一组数据，用空格隔开：")
list1 = list(inp.split(" "))
listnum1 = []
for i in list1:
    listnum1.append(int(i))
print("该组数据从小到大排序为：",sortarray(listnum1))