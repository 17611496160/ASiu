import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "gloria654",database = "作业10")

c = db.cursor()

#① 查询所有男生的姓名，年龄，所在班级名称
print("① 查询所有男生的姓名，年龄，所在班级名称：")
f = open(r"C:\ASiu\homework10\SQL\10.1.1.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#② 查询所有查询编号小于4或没被删除的学生；
print("② 查询所有查询编号小于4或没被删除的学生：")
f = open(r"C:\ASiu\homework10\SQL\10.1.2.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#③ 查询姓黄并且“名”是一个字的学生；
print("③ 查询姓黄并且“名”是一个字的学生：")
f = open(r"C:\ASiu\homework10\SQL\10.1.3.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#④ 查询编号是1或3或8的学生
print("④ 查询编号是1或3或8的学生：")
f = open(r"C:\ASiu\homework10\SQL\10.1.4.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#⑤ 查询编号为3至8的学生
print("⑤ 查询编号为3至8的学生：")
f = open(r"C:\ASiu\homework10\SQL\10.1.5.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#⑥ 查询未删除男生信息，按年龄降序
print("⑥ 查询未删除男生信息，按年龄降序：")
f = open(r"C:\ASiu\homework10\SQL\10.1.6.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
print("\n")
print("\n")

#⑦  查询女生的总数
print("⑦  查询女生的总数：")
f = open(r"C:\ASiu\homework10\SQL\10.1.7.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
print("女生总数：",len(result))
print("\n")
print("\n")

#⑧  查询学生的平均年龄
print("⑧  查询学生的平均年龄：")
f = open(r"C:\ASiu\homework10\SQL\10.1.8.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
print("年龄平均数为：",result[0][0])
print("\n")
print("\n")

#⑨ 分别统计性别为男/女的人年龄平均值
print("⑨ 分别统计性别为男/女的人年龄平均值：")
f = open(r"C:\ASiu\homework10\SQL\10.1.9m.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
print("男生的平均年龄：",result[0][0])
f = open(r"C:\ASiu\homework10\SQL\10.1.9f.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
print("女生的平均年龄：",result[0][0])
print("\n")
print("\n")

#⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
print("按照性别分组后：")
f = open(r"C:\ASiu\homework10\SQL\10.1.10.sql","r",encoding = "UTF8")
sql = f.read()
c.execute(sql)
result = c.fetchall()
for item in result:
    print(item)
