# -*- encoding: utf-8 -*-
'''
@File : dec__runtime.py
@Time : 2020/04/08 16:58:03
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 1  编写一个装饰器，能计算其他函数的运行时间；
import time
def outer(f):
    def runtime(*args,**kw):
        start_time = time.time()
        f(*args,**kw)
        end_time = time.time()
        print("该程序的运行时间为：%f"%(end_time - start_time))
    return runtime

@outer
def plus(a,b):
    print("二者之和为：" + str(a + b))

plus(1,6)