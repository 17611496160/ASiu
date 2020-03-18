# -*- encoding: utf-8 -*-
'''
@File : statistics.py
@Time : 2020/03/06 21:04:11
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 10  给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#    提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#     先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中
article = input("请输入一段英文：")
art = article.split(" ")
dict1 = {}
for i in art:
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1[i]+1
print(sorted(dict1.items(),key = lambda x:x[1],reverse = True))
