# -*- encoding: utf-8 -*-
'''
@File : get_address.py
@Time : 2020/04/20 16:20:14
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#    提示，文件有1000行，注意控制每次读取的行数；
import re
f = open(r"C:\Users\fzs\Desktop\webspiderUrl.txt","r",encoding = "UTF8")
f1 = open(r"C:\ASiu\homework7\url链接信息.txt","w",encoding = "UTF8")
for line in f.readlines():
    ret = re.search(r"http\://(\w{3})*\.*[-a-zA-Z0-9\u4E00-\u9FA5\s]*\.*[a-zA-Z0-9\u4E00-\u9FA5\s]*\.[a-zA-Z0-9\u4E00-\u9FA5\s]+(.org)*(.com)*(.net)*(.cn)*",line)
    f1.writelines(ret.group() + "\n")
    print(ret.group())
f1.close()
f.close()
