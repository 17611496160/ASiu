# -*- encoding: utf-8 -*-
'''
@File : 4server.py
@Time : 2020/05/06 10:29:55
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 服务器端
import get
import socket
import threading
import os

class Chatserver:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.add = (get.getip(),10000)
        self.user = {}
    
    def start(self):
        try:
            self.sock.bind(self.add)
        except:
            print("程序出错！")
        self.sock.listen(5) 
        print("服务器已开启，正在等待连接...")
        self.accept_cont()

    def accept_cont(self):
        while True:
            s,add = self.sock.accept()
            self.user[add] = s
            num = len(self.user)
            print("您已经连接成功，目前共有{}位用户".format(num))
            threading.Thread(target = self.recv_send,args = (s,add)).start()

    def recv_send(self,sock,add):
        while True:
            try:
                response = sock.recv(4096).decode("gbk")
                mes = "{}{}发来消息：{}".format(get.gettime(),add,response)
                for client in self.user.values():
                    client.send(mes.encode("gbk"))
            except ConnectionResetError:
                print("{}已退出聊天".format(add))
                self.user.pop(add)
                break

    def closeserver(self):
        for client in self.user.values():
            client.close()
        self.sock.close()
        os._exit()

if __name__ == "__main__":
    server = Chatserver()
    server.start()
    while True:
        cmd = input()
        if cmd == "stop sever":
            server.closeserver()
        else:
            print("输入命令无效！")