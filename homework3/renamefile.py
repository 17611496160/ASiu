# -*- encoding: utf-8 -*-
'''
@File : renamefile.py
@Time : 2020/03/27 10:01:14
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
# 将当前img目录所有以.png结尾的后缀名改为.jpg.
import os

def modifyfilename(dirname):
    filename = []
    for file in os.listdir(dirname):
        filename.append(file)
    #文件重命名
    for a in filename:
        old = os.path.join(dirname,a)
        new = os.path.join(dirname,a[:5]+'jpg')#此处''内的内容为目标格式，可以按照需求随意更改
        os.rename(old,new)
    print("修改完成")

modifyfilename(r'C:\Users\fzs\Desktop\阿siu python\homework3\img')