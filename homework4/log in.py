# -*- encoding: utf-8 -*-
'''
@File : log in.py
@Time : 2020/03/31 21:44:19
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
import hashlib

f = open(r"C:\Users\fzs\Desktop\阿siu python\homework4\userinfo.txt","r")
h = hashlib.sha256()
line = f.readline()
list = []
while line:
    list.append(line)
    line = f.readline()
list = list[1:6]
list1 = []
temp1 = list[0].strip().split("          ")
list1.append(temp1)
temp2 = list[1].strip().split("          ")
list1.append(temp2)
temp3 = list[2].strip().split("          ")
list1.append(temp3)
temp4 = list[3].strip().split("          ")
list1.append(temp4)
temp5 = list[4].strip().split("          ")
list1.append(temp5)
print(list1)
name = input("请输入您的姓名：")
for i in list1:
    if name in i:
        username = input("请输入您的账号：")
        if username in i:
            password = input("请输入您的密码：")
            h.update(bytes(password, encoding='utf-8'))
            password1 = h.hexdigest()
            if password1 in i:
                print("登陆成功！")
            else:
                print(password1)
                print("您输入的密码不正确，登陆失败！")
        else:
            print("您输入的账号不正确，登陆失败！")
    else:
        continue


