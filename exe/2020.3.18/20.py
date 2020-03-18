# 练习4
# :   一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
#             姓名      学号      分数
#             张三      101         78
#             李四      102         87
#             王五       103        83
f = open(r"C:\Users\fzs\Desktop\阿siu python\lulala.txt","r",encoding='UTF8')
f1 = open(r"C:\Users\fzs\Desktop\阿siu python\lula.txt","w")
l = f.readlines()
print(l)
list = []
list1 = []
list.append(l[2].strip().split("            "))
list.append(l[3].strip().split("            "))
list.append(l[4].strip().split("            "))
temp1 = " ".join(list[0])
temp2 = " ".join(list[1])
temp3 = " ".join(list[2])
list1.append(temp1.split("      "))
list1.append(temp2.split("      "))
list1.append(temp3.split("      "))
list1.sort(key = lambda x:x[2],reverse = True)
print(list1)
str1 = "排序后：\n"
f1.write(str1)
str2 = "姓名      学号      成绩\n"
f1.write(str2)
for i in list1:
    a = "      ".join(i)+"\n"
    f1.write(a)

f.close()
f1.close()