# -*- encoding: utf-8 -*-
'''
@File : cal.py
@Time : 2020/03/09 16:51:47
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
def calculate(m,n):
    if "+" in m:
        return n[0] + n[1]
    if "-" in m:
        return n[0] - n[1]
    if "*" in m:
        return n[0] * n[1]
    if "/" in m:
        return n[0] / n[1]

temp = input("请输入一个式子，符号与式子用空格隔开：")
eq = list(temp.split(" "))
eq1 = []
for i in eq:
    if i == '+':
        continue
    elif i == '-':
        continue
    elif i == '*':
        continue
    elif i == '/':
        continue
    else:
        eq1.append(int(i))

print("结果是：",calculate(eq,eq1))
