# 练习3:   一个文件内容的如下,请读取文件的内容, 并输出;
#             姓名      学号      分数
#             张三      101         78
#             李四      102         87
#             王五       103        83
f = open(r"C:\Users\fzs\Desktop\阿siu python\lulala.txt","r",encoding='UTF8')
for line in f.readlines():
    print(line.strip())

f.close()