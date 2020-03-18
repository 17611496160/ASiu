# -*- encoding: utf-8 -*-
'''
@File : statistics-character.py
@Time : 2020/03/08 20:56:12
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
def sc(str):
    letter = 0
    num = 0
    space = 0
    other = 0
    for ch in str:
        if ch.isalpha():
            letter += 1
        elif ch.isnumeric():
            num += 1
        elif ch.isspace():
            space += 1
        else:
            other += 1
    print("该字符串中的字母有%d个"%letter)
    print("该字符串中的数字有%d个"%num)
    print("该字符串中的空格有%d个"%space)
    print("该字符串中的其他字符有%d个"%other)
    

string = input("请输入一行字符串：")
sc(string)