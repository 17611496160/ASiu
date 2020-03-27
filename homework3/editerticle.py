# -*- encoding: utf-8 -*-
'''
@File : editerticle.py
@Time : 2020/03/27 10:00:30
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 文件编程小项目
try:
    list = []
    f = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\Blowing in the wind.txt","r",encoding = "UTF8")
    line = f.readline()
    while line:
        list.append(line)
        line = f.readline()
    list.insert(0,"Blowing in the wind")
    list.insert(1,"Bob Dylan")
    list.insert(len(list),"1962 by Warner Bros.Inc")
    for item in list:
        print(item)
    f.close()
except FileNotFoundError:
    print("未找到该文件，请检查路径")