# -*- encoding: utf-8 -*-
'''
@File : dictionary.py
@Time : 2020/03/08 21:10:45
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def refresh(dict):
    newdict = {}
    for key,value in dict.items():
        if len(value) > 2:
            newdict[key] = value[0:2]
        else:
            newdict[key] = value
    return newdict

d = {'siusingyu':'212','阿siu':'1241','草帽小子':'21'}
print("新字典为：",refresh(d))
