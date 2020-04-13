# -*- encoding: utf-8 -*-
'''
@File : password_need.py
@Time : 2020/04/08 17:58:50
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

#3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
def recog(f):
    def login(*args,**kw):
        username = input("请输入您的帐号：")
        password = input("请输入您的密码：")
        if username == 'ASiu' and password == '123456':
            f(*args,**kw)
        else:
            print("账号或密码错误请检查！")
    return login

@recog
def plus(a,b):
    print("两者之和为：" + str(a + b))

plus(1,3)
