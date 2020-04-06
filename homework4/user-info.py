# -*- encoding: utf-8 -*-
'''
@File : user-info.py
@Time : 2020/03/29 19:02:37
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX 
import hashlib

f = open(r"C:\Users\fzs\Desktop\阿siu python\homework4\userinfo.txt","w")
h = hashlib.sha256()
count = 0
while count < 5:
    name = input("请输入第" + str(count + 1) + "个同学的姓名：")
    username = input("请输入账号：")
    password = input("请输入密码：")
    h.update(bytes(password, encoding='utf-8'))
    password1 = h.hexdigest()
    if count == 0:
        f.writelines("姓名      账号        密码(已加密)" + '\n')
    temp = name + '          ' + username + '          ' + password1
    f.writelines(temp + '\n')
    count += 1
