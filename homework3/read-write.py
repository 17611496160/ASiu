# -*- encoding: utf-8 -*-
'''
@File : read-write.py
@Time : 2020/03/27 10:01:05
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
print("请输入一段文字：")
list = []
while True:
    str1 = input()
    if str1:
        list.append(str1 + '\n')
    else:
        break

try:
    f = open(r'C:\Users\fzs\Desktop\阿siu python\homework3\input.txt',"w",encoding = 'UTF8')
    for line in list:
        f.writelines(line)
    f.close()
except FileNotFoundError:
    print("未找到该文件")
except TypeError:
    print("内容格式不正确，无法写入文件，请检查！")