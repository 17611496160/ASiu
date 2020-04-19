# -*- encoding: utf-8 -*-
'''
@File : dogman.py
@Time : 2020/04/19 15:59:27
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 请写一个小游戏，人狗大站;  规则:
#     1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#         人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#         人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#     3   对战规则: 
#      A  随机决定,谁先开始攻击; 
#      B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
# 提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）
import random
class Human:
    name = ''
    atk = 0
    Lp = 0
    def __init__(self,n,atk,Lp):
        self.name = n
        self.atk = atk
        self.Lp = Lp
    
    def attack(self,dog):
        if self.atk <= 0:
            dog.LP -= 0
            print("%s被%s攻击了--------%s还剩%d点血量,剩余攻击力为%d"%(dog.name,self.name,dog.name,dog.LP,dog.Atk))
        else:
            dog.LP -= self.atk
            dog.Atk -= 3
            print("%s被%s攻击了--------%s还剩%d点血量,剩余攻击力为%d"%(dog.name,self.name,dog.name,dog.LP,dog.Atk))
    
class Dog:
    name = ''
    Atk = 0
    LP = 0
    def __init__(self,n,Atk,LP):
        self.name = n
        self.Atk = Atk
        self.LP = LP

    def attack(self,human):
        if self.Atk <= 0:
            human.Lp -= 0
            print("%s被%s攻击了---------%s还剩%d点血量,剩余攻击力为%d"%(human.name,self.name,human.name,human.Lp,human.atk))
        else:
            human.Lp -= self.Atk
            human.atk -= 2
            print("%s被%s攻击了---------%s还剩%d点血量,剩余攻击力为%d"%(human.name,self.name,human.name,human.Lp,human.atk))

print("游戏开始")
h1 = Human("Tom",10,100)
h2 = Human("Jack",10,100)
hu = []
hu.append(h1)
hu.append(h2)
d1 = Dog("小黑",15,80)
d2 = Dog("大白",15,80)
d3 = Dog("蒜黄",15,80)
do = []
do.append(d1)
do.append(d2)
do.append(d3)
flag = random.randint(1,2)
while len(hu) != 0 and len(do) != 0:
    
        

    if flag == 1:
        target = random.sample(do,1)
        attacker = random.sample(hu,1)
        attacker[0].attack(target[0])
        flag = 2

    elif flag == 2:
        target1 = random.sample(hu,1)
        attacker1 = random.sample(do,1)
        attacker1[0].attack(target1[0])
        flag = 1

    for item in do:
        if item.LP <= 0:
            do.remove(item)
    
    for item in hu:
        if item.Lp <= 0:
            hu.remove(item)

if len(hu) == 0:
    print("这场比赛狗获胜")
else:
    print("这场比赛人获胜")
    