# -*- encoding: utf-8 -*-
'''
@File : read-print.py
@Time : 2020/03/27 10:00:41
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#1.#第一行： xxxx
#2.#第二行： xxxx
try:
    list = []
    f = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\input.txt","r",encoding = "UTF8")
    line = f.readline()
    while line:
        list.append(line)
        line = f.readline()
    for i in range(len(list)):
        print("%d.#第%d行：%s"%(i+1,i+1,list[i]))
    f.close()
except FileNotFoundError:
    print("未找到该文件，请检查路径")