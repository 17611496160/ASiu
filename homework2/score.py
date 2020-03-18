# -*- encoding: utf-8 -*-
'''
@File : score.py
@Time : 2020/03/09 15:17:24
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

#  7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#     A---成绩>=90;  
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70
import random

def judge(m,n):
    if n >= 90:
        print("同学%s的成绩为A"%m)
    elif n >= 80 and n < 90:
        print("同学%s的成绩为B"%m)    
    elif n >= 70 and n < 80:
        print("同学%s的成绩为C"%m)
    elif n < 70:
        print("同学%s的成绩为D"%m)


score = {}
name = ['张三','李四','王五','阿siu','siusingyu','草帽','露西亚','露娜','火子哥','陈晖洁','黑猫警长','海绵宝宝','喜羊羊','艾斯','白胡子','嬴政','蜘蛛侠','钢铁侠','蝙蝠侠','假面骑士']
for i in name:
    score[i] = random.randint(40,100)
print(score)
for key in score:
    judge(str(key),int(score[key]))
