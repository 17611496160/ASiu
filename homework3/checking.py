# -*- encoding: utf-8 -*-
'''
@File : checking.py
@Time : 2020/03/27 10:00:14
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#     比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
import os
import json

f1 = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\英文文献1.txt","r",encoding = "UTF8")
f2 = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\英文文献2.txt","r",encoding = "UTF8")
f3 = open(r"C:\Users\fzs\Desktop\阿siu python\homework3\统计结果.txt","w",encoding = "UTF8")
f3.writelines("第一篇文章的字数："+'\n')

list1 = []
list2 = []
line1 = f1.readline()
line2 = f2.readline()
while line1:
    list1.append(line1)
    line1 = f1.readline()
dict1 = {}
for item in list1:
    temp = item.split(" ")
    for i in temp:
         if i not in dict1.keys():
            dict1[i] = 1
         else:
            dict1[i] = dict1[i]+1
dict1_sort = sorted(dict1.items(),key = lambda x:x[1],reverse = True)
json.dump(dict1_sort,f3)
f3.writelines('\n'+'\n'+'\n'+'\n'+"第二篇文章的字数："+'\n')
dict2 = {}
while line2:
    list2.append(line2)
    line2 = f2.readline()
dict2 = {}
for item in list2:
    temp = item.split(" ")
    for i in temp:
         if i not in dict2.keys():
            dict2[i] = 1
         else:
            dict2[i] = dict2[i]+1
dict2_sort = sorted(dict2.items(),key = lambda x:x[1],reverse = True)
json.dump(dict2_sort,f3)

#比较出现频率最高的前30个单词
dict1_sort = dict1_sort[:30]
dict2_sort = dict2_sort[:30]
key1 = []
key2 = []
for i in dict1_sort:
    key1.append(i[0])
print(key1)
for i in dict2_sort:
    key2.append(i[0])
print(key2)
similar = [x for x in key1 if x in key2]
print(similar)
length = (len(similar) / len(key1))
simi_str = "这两篇文章的相似度为：{:.2%}".format(length)
f3.writelines('\n'+'\n'+'\n'+'\n'+simi_str)
print("这两篇文章的相似度为：{:.2%}".format(length))
f1.close()
f2.close()
f3.close()