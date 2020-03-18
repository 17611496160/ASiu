# -*- encoding: utf-8 -*-
'''
@File : find-odds.py
@Time : 2020/03/06 15:46:35
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''
#1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
def judge(n):
    if n <= 1:
        return False
    for temp in range(2,n):
        if n % temp == 0:
            return False
    return True


zhishu = []
for i in range(1,51):
    if judge(i):
        zhishu.append(i)


print("0到50之间的偶数为：",list(x for x in range(0,51) if x % 2 == 0))
print("0到50之间的奇数为：",list(x for x in range(0,51) if x % 2 == 1))
print("0到50之间的质数为：",zhishu)
print("0到50之间能被2和3整除的数有：",list(x for x in range(0,51) if x % 2 == 0 and x % 3 == 0))