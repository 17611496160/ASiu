# -*- encoding: utf-8 -*-
'''
@File : decorate.py
@Time : 2020/04/08 18:25:17
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
import datetime
def log(f):
    def writelog(*args,**kw):
        now = datetime.datetime.now()
        strtime = now.strftime("%Y-%m-%d %H:%M:%S")
        print(strtime + "调用了函数" + f.__name__)
        return f(*args,**kw)
    return writelog

def judge(n):
    if n <= 1:
        return False
    for temp in range(2,n):
        if n % temp == 0:
            return False
    return True

@log
def print_primeA():
    sushu = []
    for i in range(1,20001):
        if judge(i):
            sushu.append(i)
    print("1-20000之间的素数有：",sushu)

@log
def print_primenumB():
    sushu = []
    for i in range(1,20001):
        if judge(i):
            sushu.append(i)
    return len(sushu)

@log
def print_primenumC(a):
    sushu = []
    for i in range(1,a):
        if judge(i):
            sushu.append(i)
    return len(sushu)

print_primeA()
print("1-20000之间的素数有%d个"%print_primenumB())
print("1-%d之间的素数有%d个"%(300,print_primenumC(300)))