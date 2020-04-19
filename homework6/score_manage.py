# -*- encoding: utf-8 -*-
'''
@File : score_manage.py
@Time : 2020/04/14 19:21:46
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;
class student():
    cla = ""
    ID = ""
    name = ""
    score = ""
    file = open(r"C:\ASiu\homework6\studentscore.txt","w",encoding = 'UTF8')
    file.write("班级" + "\t\t" + "学号" + "\t\t" + "姓名" + "\t\t" + "Python成绩" + "\n")
    file.close()
    def __init__(self,a,b,c,d):
        self.cla = a
        self.ID = b
        self.name = c
        self.score = d
        

    def add(self):
        f1 = open(r"C:\ASiu\homework6\studentscore.txt","a")
        f1.write(self.cla + "\t\t" + self.ID + "\t\t" + self.name + "\t\t" + self.score + "\n")
        print("填入完毕")
        f1.close()

    def delete(self):
        f = open(r"C:\ASiu\homework6\studentscore.txt","r",encoding = 'UTF8')
        con = []
        for line in f.readlines():
            con.append(line.strip().split("\t\t"))
        print("删除前的文件内容：",con)
        f.close()
        for item in con:
            if self.ID in item:
                con.remove(item)
        print("删除后的文件内容：",con)
        f2 = open(r"C:\ASiu\homework6\studentscore.txt","w",encoding = 'UTF8')
        for item in con:
            f2.write("\t\t".join(item) + '\n')
        f2.close()
    
    def update(self):
        f3 = open(r"C:\ASiu\homework6\studentscore.txt","r",encoding = 'UTF8')
        con = []
        for line in f3.readlines():
            con.append(line.strip().split("\t\t"))
        print("修改前的文件内容：",con)
        f3.close()
        for item in con:
            if self.name in item:
                item[0] = self.cla
                item[1] = self.ID
                item[3] = self.score
        print("修改后的文件内容：",con)
        f4 = open(r"C:\ASiu\homework6\studentscore.txt","w",encoding = 'UTF8')
        for item in con:
            f4.write("\t\t".join(item) + '\n')
        f4.close()
    
    def search(self):
        f5 = open(r"C:\ASiu\homework6\studentscore.txt","r",encoding = 'UTF8')
        con = []
        for line in f5.readlines():
            con.append(line.strip().split("\t\t"))
        f5.close()
        for item in con:
            if self.name in item:
                print("{0}的班级是{1}班，学号为{2}，Python成绩为{3}".format(self.name,item[0],item[1],item[3]))
        
        





while 1:
    choice = int(input("请输入您想要的操作序号(1.添加信息 2.删除信息 3.修改信息 4.查找信息)："))
    if choice == 1:
        cla = input("请输入班级：")
        ID = input("请输入学号：")
        name = input("请输入姓名：")
        score = input("请输入python成绩：")
        stu = student(cla,ID,name,score)
        stu.add()
    if choice == 2:
        ID1 = input("请输入需要删除的学生学号：")
        stu1 = student(None,ID1,None,None)
        stu1.delete()
    if choice == 3:
        cla2 = input("请输入修改后的班级：")
        ID2 = input("请输入修改后的学号：")
        name2 = input("请输入需要修改的学生姓名：")
        score2 = input("请输入修改后的python成绩：")
        stu2 = student(cla2,ID2,name2,score2)
        stu2.update()
    if choice == 4:
        name3 = input("请输入需要查询的学生姓名：")
        stu3 = student(None,None,name3,None)
        stu3.search()
    flag = input("继续操作吗？Y/N：")
    if flag == 'N' or flag == 'n':
        break
