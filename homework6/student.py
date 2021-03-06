# -*- encoding: utf-8 -*-
'''
@File : student.py
@Time : 2020/04/14 17:04:06
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class Student:
    name = ''
    age = 0
    chinese = ''
    math = ''
    english = ''
    def __init__(self,name,age,chinese,math,english):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_course(self):
        return max(self.chinese,self.math,self.english)

stu1 = Student("ASiu",20,80,70,100)
print("该同学的名字为：",stu1.get_name())
print("该同学的年龄为：%d"%stu1.age)
print("该同学的最高成绩为：%d"%stu1.get_course())