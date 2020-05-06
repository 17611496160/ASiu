# -*- encoding: utf-8 -*-
'''
@File : anti_test.py
@Time : 2020/05/03 21:06:11
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
from socket import *

upsocket = socket(AF_INET,SOCK_DGRAM)
local = ('',9999)
upsocket.bind(local)
getdata = upsocket.recvfrom(1024)
print(getdata)
upsocket.close()