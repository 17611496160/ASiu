# -*- encoding: utf-8 -*-
'''
@File : 3client.py
@Time : 2020/05/04 16:41:19
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
# from socket import *
# import time

# s = socket(AF_INET,SOCK_DGRAM)
# for data in [b'Michael',b'Tracy',b'Sarah']:
#     s.sendto(data,('127.0.0.1',9999))
#     print(s.recv(1024).decode('UTF8'))
# s.close()

from socket import *
import time

s = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("请输入您的姓名：")
    data = data.encode()
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('UTF8'))

s.close()