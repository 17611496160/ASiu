# -*- encoding: utf-8 -*-
'''
@File : python Pro.py
@Time : 2020/06/22 19:48:29
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# python大作业

from bs4 import BeautifulSoup
import requests
import chardet
from lxml import etree
import re
import threading

def get_content(page):  # 获取每页全部的html信息
    # 爬取的页面 url
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99°reefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(page)
    # 设置代理信息 伪装成浏览器访问
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

    request = requests.get(url, headers=headers)

    # 字符转码
    request.encoding = chardet.detect(request.content)['encoding']
    request.encoding = "iso-8859-1"
    html = request .content.decode('iso-8859-1').encode('iso-8859-1')

    soup = BeautifulSoup(html, 'lxml')
    soup.prettify()  # 格式化soup对象

    return soup

mutex = threading.Lock() # 设置互斥锁
Name = []  # 初步存储职位名称信息（结果带有\n\n）
Name1 = []  # 存储最终的职位名称（结果去除特殊符号）
Company = []  # 公司名称
Location = []  # 工作地点
Salary = []  # 薪资
Published = []  # 发布时间
def getinfo1():
    for i in range(1, 11):  # 循环爬取1-10页数据
        soup = get_content(i)
        # 名称
        name = soup.find_all('p', class_="t1")  # 用 find_all 方法搜索所有 class为t1 的 p 对象
        for n in name:
            mutex.acquire()
            Name.append(n.get_text())  # 提取名称加入到 Name列表中
            mutex.release()
        # 公司名称
        company = soup.find_all('span', class_="t2")
        for i in company:
            mutex.acquire()
            Company.append(i.get_text())  # 提取公司名称加入到Company列表中
            mutex.release()
        # 工作地点
        location = soup.find_all('span', class_="t3")
        for i in location:
            mutex.acquire()
            Location.append(i.get_text())  # 提取工作地点加入到Location列表中
            mutex.release()
        # 薪资情况
        salary = soup.find_all('span', class_="t4")
        for i in salary:
            mutex.acquire()
            Salary.append(i.get_text())  # 提取薪资加入到Salary列表中
            mutex.release()
        # 发布时间
        published = soup.find_all('span', class_="t5")
        for i in published:
            mutex.acquire()
            Published.append(i.get_text())  # 提取发布时间加入到Published列表中
            mutex.release()


def getinfo2():
    for i in range(11, 21):  # 循环爬取11-20页数据
        soup = get_content(i)
        name = soup.find_all('p', class_="t1")
        for n in name:
            mutex.acquire()
            Name.append(n.get_text())
            mutex.release()
        company = soup.find_all('span', class_="t2")
        for i in company:
            mutex.acquire()
            Company.append(i.get_text())
            mutex.release()
        location = soup.find_all('span', class_="t3")
        for i in location:
            mutex.acquire()
            Location.append(i.get_text())
            mutex.release()
        salary = soup.find_all('span', class_="t4")
        for i in salary:
            mutex.acquire()
            Salary.append(i.get_text())
            mutex.release()
        published = soup.find_all('span', class_="t5")
        for i in published:
            mutex.acquire()
            Published.append(i.get_text())
            mutex.release()


def getinfo3():
    for i in range(21, 31):  # 循环爬取21-30页数据
        soup = get_content(i)
        name = soup.find_all('p', class_="t1")
        for n in name:
            mutex.acquire()
            Name.append(n.get_text())
            mutex.release()
        company = soup.find_all('span', class_="t2")
        for i in company:
            mutex.acquire()
            Company.append(i.get_text())
            mutex.release()
        location = soup.find_all('span', class_="t3")
        for i in location:
            mutex.acquire()
            Location.append(i.get_text())
            mutex.release()
        salary = soup.find_all('span', class_="t4")
        for i in salary:
            mutex.acquire()
            Salary.append(i.get_text())
            mutex.release()
        published = soup.find_all('span', class_="t5")
        for i in published:
            mutex.acquire()
            Published.append(i.get_text())
            mutex.release()


def getinfo4():
    for i in range(31,38):  # 循环爬取31-37页数据
        soup = get_content(i)
        name = soup.find_all('p', class_="t1")
        for n in name:
            mutex.acquire()
            Name.append(n.get_text())
            mutex.release()
        company = soup.find_all('span', class_="t2")
        for i in company:
            mutex.acquire()
            Company.append(i.get_text())
            mutex.release()
        location = soup.find_all('span', class_="t3")
        for i in location:
            mutex.acquire()
            Location.append(i.get_text())
            mutex.release()
        salary = soup.find_all('span', class_="t4")
        for i in salary:
            mutex.acquire()
            Salary.append(i.get_text())
            mutex.release()
        published = soup.find_all('span', class_="t5")
        for i in published:
            mutex.acquire()
            Published.append(i.get_text())
            mutex.release()

def main():
    t1 = threading.Thread(target = getinfo1)
    t2 = threading.Thread(target = getinfo2)
    t3 = threading.Thread(target = getinfo3)
    t4 = threading.Thread(target = getinfo4)
    t1.run()
    t2.run()
    t3.run()
    t4.run()
    for a in Name:
        Name1.append(a.strip())  # 提取 Name 中的职位名称
    Name1.insert(0, '职位')  # Name1 列表中插入“职位” 以保证数据对应

    # 将获取到的数据打印出来
    bj_salary = []  # 用于存放北京地区的薪资情况
    for item in list(zip(Name1, Company, Location, Salary, Published)):
        if '北京' in item[2]:
            print(item)
            bj_salary.append(item[3])
    print("北京地区的薪资情况",bj_salary)
    low_salary = [] # 进一步划分高、低水平薪资情况
    high_salary = []
    for i in bj_salary:
        if "年" in i:  # 结果中有年薪 转化为月薪
            ret = re.findall(r"\d+\.?\d*",i)
            low_salary.append((float(ret[0]) * 10000)/ 12)
            high_salary.append((float(ret[0]) * 10000)/ 12)
        if "月" in i:
            ret = re.findall(r"\d+\.?\d*",i)
            if "万" in i:
                low_salary.append(float(ret[0]) * 10000)
                high_salary.append(float(ret[0]) * 10000)
            elif "千" in i:
                low_salary.append(float(ret[0]) * 1000)
                high_salary.append(float(ret[0]) * 1000)
        if "天" in i:  # 结果中日新 转化为月薪
            ret = re.findall(r"\d+\.?\d*",i)
            low_salary.append(float(ret[0]) * 30)

        
    print("北京地区低水平薪资情况",low_salary)
    print("北京地区高水平薪资情况",high_salary)
    low = sum(low_salary) / len(low_salary)
    high = sum(high_salary) / len(high_salary)
    print("北京地区的平均薪资水平为%.3f-%.3f"%(low,high))

main()