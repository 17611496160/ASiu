# -*- encoding: utf-8 -*-
'''
@File : multiprocess.py
@Time : 2020/04/26 19:34:21
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
import threading
import time

def judge(n):
    if n <= 1:
        return False
    for temp in range(2,n):
        if n % temp == 0:
            return False
    return True

def count(m,n):
    zhishu = []
    for i in range(m,n):
        if judge(i):
            zhishu.append(i)
    print("{0}与{1}之间的素数有{2}个".format(m,n - 1,len(zhishu)))

#----------对比1----------
start = time.time()
count(1,100001)
end = time.time()
p1 = threading.Thread(count(1,20001))
p2 = threading.Thread(count(20001,40001))
p3 = threading.Thread(count(40001,60001))
p4 = threading.Thread(count(60001,80001))
p5 = threading.Thread(count(80001,100001))
start1 = time.time()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
end1 = time.time()
if len(threading.enumerate()) == 1:
    print("不使用多进程：%f"%(end - start))
    print("使用多进程：%f"%(end1 - start1))

#----------对比2----------
p6 = threading.Thread(count(1,25001))
p7 = threading.Thread(count(25001,50001))
p8 = threading.Thread(count(50001,75001))
p9 = threading.Thread(count(75001,100001))
start2 = time.time()
p6.start()
p7.start()
p8.start()
p9.start()
end2 = time.time()
p10 = threading.Thread(count(1,10001))
p11 = threading.Thread(count(10001,20001))
p12 = threading.Thread(count(20001,30001))
p13 = threading.Thread(count(30001,40001))
p14 = threading.Thread(count(40001,50001))
p15 = threading.Thread(count(50001,60001))
p16 = threading.Thread(count(60001,70001))
p17 = threading.Thread(count(70001,80001))
p18 = threading.Thread(count(80001,90001))
p19 = threading.Thread(count(90001,100001))
start3 = time.time()
p10.start()
p11.start()
p12.start()
p13.start()
p14.start()
p15.start()
p16.start()
p17.start()
p18.start()
p19.start()
end3 = time.time()
if len(threading.enumerate()) == 1:
    print("4个多进程：%f"%(end2 - start2))
    print("10个多进程：%f"%(end3 - start3))


