# -*- encoding: utf-8 -*-
'''
@File : UDP.py
@Time : 2020/05/04 16:18:40
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
from socket import *
import time
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
while True:
    data,add = s.recvfrom(1024)
    s.sendto(b'hello,%s'%data,add)