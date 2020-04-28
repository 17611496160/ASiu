# -*- encoding: utf-8 -*-
'''
@File : communication.py
@Time : 2020/04/28 17:26:13
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''


# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
from multiprocessing import Process,Queue
import os,time,random

def write(q,value):
    print('Process to write: %s' % os.getpid())
    print("you've already send information: %s"%value)
    q.put(value)
    time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            print('you\'ve already received information:  %s.' % value)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    value = input("请输入您要发送的信息：")
    while value:
        pw = Process(target=write, args=(q,value))
        pr = Process(target=read, args=(q,))
        pw.start()
        pw.join()
        pr.start()
        pr.join()
        pr.terminate()
        value = input("请输入您要发送的信息：")
    
    
    # 启动子进程pw，写入:
    
    # 等待pw结束:
   
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    