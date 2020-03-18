# -*- encoding: utf-8 -*-
'''
@File : max-appear.py
@Time : 2020/03/09 16:09:24
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
# 例如，输入 aaaabbc，输出：a:4
string = input("请输入一个字符串：")
string1 = list(string)
dict1 = {}
for i in string1:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1[i]+1
print("最多出现的字符及其次数为(次数，字符)：",max(zip(dict1.values(),dict1.keys())))