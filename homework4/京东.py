# -*- encoding: utf-8 -*-
'''
@File : 京东.py
@Time : 2020/04/04 19:57:37
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
import random

def create(f):
    ip = ['172.25.254.' + str(i) for i in range(1,255)]
    file = open(f,'a+')
    count = 0
    while count < 1200:
        file.write(str(random.sample(ip,1)) + '\n')

f = open(r"C:\Users\fzs\Desktop\阿siu python\homework4\京东.txt")
create(r"C:\Users\fzs\Desktop\阿siu python\homework4\京东.txt")
ipdict = dict()
for item in f:
    item = item.strip()
    if item in ipdict:
        ipdict[item] += 1
    else:
        ipdict[item] = 1
print(sorted(ipdict.items(),key = lambda x:x[1],reverse = True)[:10])