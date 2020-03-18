# 练习:  构造上述文件结构,分别在指定位置打开文件进行写入操作;同级文件夹里面打开;  同级目录下的子目录里面打开; 上一级文件目录中的其他文件夹中打开

f = open(r'C:\Asiu\exe\2020.3.18\student.txt')
with open(r'..\b_file\file_open2.txt',"r") as file:
    print(file.readlines())