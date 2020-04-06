# -*- encoding: utf-8 -*-
'''
@File : date.py
@Time : 2020/03/29 17:59:51
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
import datetime

year = int(input("请输入当前日期的年份："))
month = int(input("请输入当前日期的月份："))
day = int(input("请输入当前日期的天份："))
result = datetime.date(year,month,day).isocalendar()
print("该日期为"+str(result[0])+"年的第"+str(result[1])+"个星期的周"+str(result[2]))
nowdatestr = str(year) + '-' + str(month) + '-' + str(day)
standarddatestr = '2020-2-17'
nowdate = datetime.datetime.strptime(nowdatestr,'%Y-%m-%d')
standarddate = datetime.datetime.strptime(standarddatestr,'%Y-%m-%d')
days = (nowdate - standarddate).days
week = days // 7
day = days % 7
print("该日期是校历第"+str(week+1)+"周"+"星期"+str(day+1))