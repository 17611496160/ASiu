# -*- encoding: utf-8 -*-
'''
@File : gussgame.py
@Time : 2020/03/06 19:26:51
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
def guess(x,number):
    i = 1
    while i < x+1:
        a = int(input("请输入第%d次猜测的数字："%i))
        if a < number:
            print("比答案小，还有%d次机会"%(x-i))
        elif a > number:
            print("比答案大，还有%d次机会"%(x-i))
        else:
            print("恭喜您猜对了！")
        i = i+1
    if i > x:
        print("您的机会已经用完，游戏失败")



temp = int(input("请输入一个数字："))
time = int(input("请输入猜测次数："))
guess(time,temp)