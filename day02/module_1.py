from day02.module_2 import a as module_2_a

# from import语句会把要导入的模块执行一遍之后再导入当前模块

a = "我是模块1中的a变量"

def name():
    print("我是模块1中的name方法")


class Test():
    name="我是模块1中的Test类"

# print(module_2_a)


import os # 路径操作
import sys
import re # 正则模块
import random # 随机模块


print(os.listdir(".")) # 显示给定文件夹下的所有文件，linux中的ls
print(os.path.exists("module_2.py")) # 判断给定的文件路径是否存在
print(os.path.abspath(".")) # 显示给定目录的绝对路径 相当于cd + pwd + 文件名
print(os.path.abspath("module_2.py"))
print(os.path.dirname(os.path.abspath("module_2.py"))) # 返回文件路径的目录
print(os.path.join("e:\\workspace","python","base_2006A","__init__.py"))
# print(os.system("dir")) # 执行cmd命令

r = re.compile("(\d+)") # 编译正则表达式
res = r.findall("sdjfisji1123123sjifjis324678sfd") # 匹配字符串并获取结果
print(res)


print(random.randint(1,10)) # 生成随机整数
print(random.choice(['1','2','3','5'])) # 随机从集合中去一个数据
print(random.choices("ajibkgiooi1239696",k=10)) # 随机从集合中选取n次数据











