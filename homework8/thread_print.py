# -*- encoding: utf-8 -*-
'''
@File : thread_print.py
@Time : 2020/04/25 18:41:49
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
import threading
import random
from multiprocessing import Pool

score = []
i = 0
j = 0
for i in range(100):
    score.append(random.randint(50,100))


def print_score():
    global score
    global j
    time = 0
    while time < 20:
        mutex.acquire()
        print("第%d个同学的分数为：%d"%(j + 1,score[j]))
        time += 1
        j += 1
        mutex.release()
    print("%s---------------------------------------------------------%d"%(threading.currentThread().name,j))

#多线程实现
mutex = threading.Lock()
p1 = threading.Thread(target = print_score)
p1.start()
p2 = threading.Thread(target = print_score)
p2.start()
p3 = threading.Thread(target = print_score)
p3.start()
p4 = threading.Thread(target = print_score)
p4.start()
p5 = threading.Thread(target = print_score)
p5.start()


#------------------------以下为进程池实现该功能-----------------------------

# score1 = []
# k = 0
# m = 0
# for k in range(100):
#     score.append(random.randint(50,100))

# def print_score1(i):
#     global score1
#     global m
#     time = 0
#     while time < 20:
#         print("第%d个同学的分数为：%d"%(m + 1,score[m]))
#         time += 1
#         m += 1
#     print("%s---------------------------------------------------------%d"%(threading.currentThread().name,m))

# #进程池实现
# if __name__ == "__main__":
#     mutex = threading.Lock()
#     po = Pool(1)
#     for i in range(0,5):
#         po.apply_async(print_score1,(i,))
#     po.close()
#     po.join()