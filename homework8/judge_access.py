# -*- encoding: utf-8 -*-
'''
@File : judge_access.py
@Time : 2020/04/28 18:33:30
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
import requests
import threading

def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        if r.text:
            print("可正常访问")
    except:
         print("访问产生异常")

f = open(r"C:\Users\fzs\Desktop\url_data.txt","r")
count = 0
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
for line in f.readlines():
    if count < 200:
        a1.append(line.strip())
    elif count >= 200 and count < 400:
        a2.append(line.strip())
    elif 400 <= count and count < 600:
        a3.append(line.strip())
        line = f.readlines()
    elif 600 <= count and count < 800:
        a4.append(line.strip())
    elif 800 <= count and count < 1000:
        a5.append(line.strip())
    count += 1
for item in range(0,200):
    p1 = threading.Thread(target = getHtmlText(a1[item]))
    p2 = threading.Thread(target = getHtmlText(a2[item]))
    p3 = threading.Thread(target = getHtmlText(a3[item]))
    p4 = threading.Thread(target = getHtmlText(a4[item]))
    p5 = threading.Thread(target = getHtmlText(a5[item]))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

f.close()