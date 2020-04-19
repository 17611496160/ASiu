# -*- encoding: utf-8 -*-
'''
@File : dog_sale.py
@Time : 2020/04/10 15:39:26
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#        实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
class Dog:
    doglist = []
    def __init__(self):
        Dog.doglist.append({'red':[5,100]})
        Dog.doglist.append({'green':[6,200]})
        Dog.doglist.append({'white':[7,300]})
    def forsale(self,num,color):
        if color == 'red':
            print("您已经购买了%d只红色小狗,共需支付%d元"%(num,num * Dog.doglist[0]['red'][1]))
            Dog.doglist[0]['red'][0] -= num
            
        if color == 'green':
            print("您已经购买了%d只绿色小狗,共需支付%d元"%(num,num * Dog.doglist[1]['green'][1]))
            Dog.doglist[1]['green'][0] -= num
        
        if color == 'white':
            print("您已经购买了%d只白色小狗,共需支付%d元"%(num,num * Dog.doglist[2]['white'][1]))
            Dog.doglist[2]['white'][0] -= num

    @staticmethod
    def print_num():
        print("红色的小狗还剩{0}只，绿色的小狗还剩{1}只，白色的小狗还剩{2}只".format(Dog.doglist[0]['red'][0],Dog.doglist[1]['green'][0],Dog.doglist[2]['white'][0]))


buyer = Dog()
num = int(input("请输入您想要购买的数量(不大于5)："))
color = input("请输入如您想要购买的品种：")
buyer.forsale(num,color)
flag = input("继续购买吗？Y/N")
if flag == 'Y' or flag == 'y':
    num = int(input("请输入您想要购买的数量(不大于5)："))
    color = input("请输入如您想要购买的品种：")
    buyer.forsale(num,color)
flag = input("继续购买吗？Y/N")
if flag == 'Y' or flag == 'y':
    num = int(input("请输入您想要购买的数量(不大于5)："))
    color = input("请输入如您想要购买的品种：")
    buyer.forsale(num,color)

buyer.print_num()
