# -*- encoding: utf-8 -*-
'''
@File : multiplelist.py
@Time : 2020/03/06 19:13:48
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 7 打印输出9*9乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d  "%(j,i,i*j),end = '')
    print("\n")
    
