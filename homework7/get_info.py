# -*- encoding: utf-8 -*-
'''
@File : get_info.py
@Time : 2020/04/22 17:37:10
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库

from bs4 import BeautifulSoup
import urllib.request

f1 = open(r"C:\ASiu\homework7\url链接信息.txt","r",encoding = "UTF8")
url = f1.readlines()
url =  url[0:100]
for item in url:
    item = item.strip()
    html = urllib.request.urlopen(item).read()
    soup = BeautifulSoup(html,features = "html.parser")
    print("%s的相关信息："%item)
    for link in soup.find_all('a'):
        if link.get('href'):
            if 'javascript' in link.get('href'):
                continue
            if 'http' in link.get('href'):
                print(link.get('href'))
            else:
                print(item + link.get('href'))
            
        else:
            continue
f1.close()

