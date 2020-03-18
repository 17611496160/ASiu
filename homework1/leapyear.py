# -*- encoding: utf-8 -*-
'''
@File : leapyear.py
@Time : 2020/03/06 16:50:08
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 4  判断用户输入的年份是否为闰年
year = int(input("请输入一个年份："))
if year % 400 == 0:
    print("%d是闰年"%year)
elif year % 4 == 0 and year % 100 != 0:
    print("%d是闰年"%year)
else:
    print("%d不是闰年"%year)