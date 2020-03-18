# 练习:
#   给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
import pickle
import io

f = open("lulala.pkl","wb")
dict = {
    'asf':[111,18],
    'sdf':[222,18],
    'dsm':[333,20],
    'sdg':[444,19],
    'jdi':[555,17]
}
pickle.dump(dict,f,-1)
f.close()       