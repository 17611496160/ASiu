# -*- encoding: utf-8 -*-
'''
@File : get.py
@Time : 2020/05/06 10:23:39
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# get模块
import socket
import datetime

def getip():
    h = socket.gethostname()
    ip = socket.gethostbyname(h)
    return ip

def gettime():
    now = datetime.datetime.now()
    showtime = now.strftime("%Y-%m-%d %H:%M:%S")
    return showtime