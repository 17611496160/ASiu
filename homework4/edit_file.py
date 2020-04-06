# -*- encoding: utf-8 -*-
'''
@File : edit_file.py
@Time : 2020/04/06 16:21:19
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
#     名称         日期                   类型（文件夹或者 文件）       大小
import os
import datetime
def gettime(ts):
    return datetime.datetime.fromtimestamp(ts)

filename = []
for file in os.listdir(r"C:\Users\fzs\Desktop\阿siu python\homework4\第六题"):
    filename.append([file])
for i in range(len(filename)):
    strname = r"C:\Users\fzs\Desktop\阿siu python\homework4\第六题" + "\\" + filename[i][0]
    time = gettime(os.stat(strname).st_atime).strftime('%Y-%m-%d %H:%M:%S')
    filename[i].append(time)
    if os.path.isfile(strname):
        filename[i].append("文件")
        filename[i].append(str(os.stat(strname).st_size) + "字节")
    else:
        filename[i].append("文件夹")

filename.insert(0,["名称","日期","类型","大小"])
print(filename)
for j in range(len(filename)):
    if j == 0:
        print("                    ".join(filename[j]))
    else:
        print("               ".join(filename[j]))