# -*- encoding: utf-8 -*-
'''
@File : stu_score.py
@Time : 2020/04/14 19:01:30
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。
class Student:
    name = ''
    age = 0
    gender = ''
    chinese = ''
    math = ''
    english = ''
    def __init__(self,name,age,gender,chinese,math,english):
        self.name = name
        self.age = age
        self.gender = gender
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def sumup(self):
        print("该学生的总分为：%d"%(self.chinese + self.math + self.english))

    def average(self):
        print("该学生的平均分为：{0}".format((self.chinese + self.math + self.english) / 3))

    def printinfo(self):
        print("该学生的姓名为{0}，年龄{1}，性别{2}，语文分数{3}，数学分数{4}，英语分数{5}".format(self.name,self.age,self.gender,self.chinese,self.math,self.english))

stu = Student("ASiu",20,"女",80,70,100)
stu.sumup()
stu.average()
stu.printinfo()