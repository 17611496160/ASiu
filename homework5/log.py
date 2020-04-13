# -*- encoding: utf-8 -*-
'''
@File : log.py
@Time : 2020/04/08 17:24:27
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
import datetime
def log(f):
    def writelog(*args,**kw):
        now = datetime.datetime.now()
        strtime = now.strftime("%Y-%m-%d %H:%M:%S")
        file = open(r"C:\ASiu\homework5\log.txt","a")
        text = strtime + "调用了函数" + f.__name__
        file.writelines(text)
        file.close()
        return f(*args,**kw)
    return writelog

@log
def plus(a,b):
    print("二者之和为：" + str(a + b))

plus(1,6)