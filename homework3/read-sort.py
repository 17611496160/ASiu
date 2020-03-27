# -*- encoding: utf-8 -*-
'''
@File : read-sort.py
@Time : 2020/03/27 10:00:53
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
try:
    list = []
    f = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\student-score.txt","r",encoding = "UTF8")
    line = f.readline()
    while line:
        list.append(line)
        line = f.readline()
    f.close()
    for i in range(len(list)):
        list[i] = list[i].split()
    list = list[1:len(list)]
    for j in range(len(list)):
        list[j][2] = int(list[j][2])
    list.sort(key = lambda x:x[2],reverse = True)
    for k in range(len(list)):
        list[k][2] = str(list[k][2])
    print("学号     姓名     python成绩")
    for ele in list:
        ele = "     ".join(ele)
        print(ele)
except FileNotFoundError:
    print("未找到该文件，请检查路径是否正确")