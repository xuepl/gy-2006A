import requests


a = "我是模块2中的a变量"

def name():
    print("我是模块2中的name方法")


class Test():
    name="我是模块2中的Test类"

'''
不是自己开发的，
不是python解释器提供的
第三方开发者提供的

第三方包，先使用`pip install 包名` 安装,然后from import语法导入到当前模块

'''





if __name__ == '__main__':
    # print(module_1.a)
    name()
    print(Test.name)

