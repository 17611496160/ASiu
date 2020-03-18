# -*- encoding: utf-8 -*-
'''
@File : student-score.py
@Time : 2020/03/06 16:25:06
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 2 一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；
score = {1:90,2:80,3:98,4:78,5:87,6:67,7:57,8:96,9:69,10:93}
for key,value in score.items():
    if value>80:
        print("学号：" + str(key) + "  成绩：" + str(value))