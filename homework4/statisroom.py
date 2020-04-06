# -*- encoding: utf-8 -*-
'''
@File : statisroom.py
@Time : 2020/04/06 17:35:50
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 7 使用python代码统计一个文件夹中所有文件的总大小
import os

filename = []
sum = 0
for file in os.listdir(r"C:\Users\fzs\Desktop\阿siu python\homework4\第六题"):
    filename.append([file])
for i in range(len(filename)):
    strname = r"C:\Users\fzs\Desktop\阿siu python\homework4\第六题" + "\\" + filename[i][0]
    if os.path.isfile(strname):
        sum += os.stat(strname).st_size
print("该文件夹中的所有文件大小为：" + str(sum) + "字节")