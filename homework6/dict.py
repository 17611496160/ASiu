# -*- encoding: utf-8 -*-
'''
@File : dict.py
@Time : 2020/04/14 18:04:02
@Author : fzs
@Version : 1.0
@Contact : fzs1116@hotmail.com
@WebSite : none
'''

# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass:
    dict = {}
    def __init__(self,dict):
        self.dict = dict

    def del_dict(self,key):
        error = "not found"
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return error

    def get_key(self):
        return list(self.dict.keys())
    
    def update_dict(self,dict1):
        self.dict.update(dict1)
        return self.dict

dict = dictclass({'a':1,'b':2,'c':3,'d':4,'e':5})
print(dict.del_dict('a'))
print(dict.del_dict('f'))
print(dict.get_key())
print(dict.update_dict({'f':6,'g':7}))