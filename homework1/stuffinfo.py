# -*- encoding: utf-8 -*-
'''
@File : stuffinfo.py
@Time : 2020/03/06 19:23:12
@Author : xdbcb8 
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : www.xdbcb8.com
'''

# 8.设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
#    提示：可以组合使用我们的序列数据类型；
def four(elem):
    return elem[3]

i = 0
listinfo1 = ('123','a',2,100)
listinfo2 = ('234','b',1,45)
listinfo3 = ('345','c',1,87)
listinfo4 = ('456','d',2,474)
listinfo5 = ('567','e',3,573)
listinfo6 = ('678','f',3,565)
listinfo7 = ('789','g',1,5)
listinfo8 = ('891','h',3,654)
listinfo9 = ('912','i',4,754)
listinfo10 = ('012','j',10,5436)
listinfo = [listinfo1,listinfo2,listinfo3,listinfo4,listinfo5,listinfo6,listinfo7,listinfo8,listinfo9,listinfo10]
listinfo.sort(key=four,reverse=True)
print('(工号, 姓名, 工龄, 工资)')
for i in range(len(listinfo)):
    print(listinfo[i])

