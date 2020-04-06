# -*- encoding: utf-8 -*-
'''
@File : copy.py
@Time : 2020/04/04 22:03:57
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 通过Python来模拟实现一个txt文件的拷贝过程;
import os

def copyfile(f1,f2):
    file1 = open(f1,'r',encoding = 'UTF8')
    file2 = open(f2,'w',encoding = 'UTF8')
    text = file1.read()
    print(text)
    file2.write(text)
    file1.close()
    file2.close()

copyfile(r"C:\Users\fzs\Desktop\阿siu python\homework4\text1.txt",r"C:\Users\fzs\Desktop\阿siu python\homework4\text2.txt")