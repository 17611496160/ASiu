# -*- encoding: utf-8 -*-
'''
@File : 4client.py
@Time : 2020/05/06 20:26:49
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 用户端
import socket
import threading
import os
import get

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
add = (get.getip(),10000)
s.connect(add)

def recv_msg():
    print("连接成功！\n")
    while True:
        try:
            response = s.recv(1024)
            print(response.decode("gbk"))
        except ConnectionResetError:
            print("服务器已关闭！")
            s.close()
            break
    os._exit(0)

def send_msg():
    print("连接成功！\n")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            s.close()
            break
        s.send(msg.encode("gbk"))
    os._exit(0)

threads = [threading.Thread(target = recv_msg),threading.Thread(target = send_msg)]
for t in threads:
    t.start()