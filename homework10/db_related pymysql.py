# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","gloria654","作业10")

#创建游标对象
cursor = db.cursor()

#添加第一条记录
sql = "insert into notepad(ID,content,people,leavetime,deleteornot) values ('0','good good study','Mac','2020-5-3 19:47:43','yes')"
#添加第二条记录
sql1 = "insert into notepad(ID,content,people,leavetime,deleteornot) values ('1','day day up','Jack','2020-5-3 21:47:43','no')"
#添加第三条记录
sql2 = "insert into notepad(ID,content,people,leavetime,deleteornot) values ('2','by ASiu','JASiu','2020-5-3 23:47:43','yes')"
#删除记录
sql3 = "delete from notepad where deleteornot = 'no'"
#查询记录
sql4 = "select * from notepad where people = 'Mac'"
try:
    cursor.execute(sql)
    cursor.execute(sql1)
    cursor.execute(sql2)
    # cursor.execute(sql3)
    db.commit()


    # cursor.execute(sql4)
    # result = cursor.fetchall()
    # for row in result:
    #     print(row[0] + "    " + row[1] + "   " + row[2] + "    " + str(row[3]) + "      " + row[4])

    print("命令执行完毕")
except Exception as e:
    print(e)
    db.rollback()

db.close()
