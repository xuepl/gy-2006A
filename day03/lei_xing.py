
'''
字符串
数字
布尔
空
列表
元组
集合
字典

'''

# a = 123
#
# b = "456"
#
#
#
#
# # 字符串转数字
#
# print(a + int(b))
# # 数字转字符串
# print(str(a) + b)
#
# # 字符串转列表 列表 元组 集合
# t = (1,2,3,4)
# l = [1,2,3,4,5,65,7]
# s = {1,2,3,4,6,9,8}
# # 字符串转列表
# print(list(b))
# # 元祖转列表
# print(list(t))
# # 列表转元祖
# print(tuple(l))
# # 元祖转集合
# print(set(t))
# # 集合转列表
# print(list(s))


# 打开模式：r 读取 w清空写入 a追加写入 b二进制模式

# f = open("aaa.txt",'w') # open打开文件
# # f.write("asdfasdf\nasfsfsf\nsfsfsfasf\n") # write写入内容至打开的文件
# # f.writelines(["safdsf\n","sdfasfasf\n","asfsafsd\n"])
# print(f.writable())# 判断是否可写入
# f.close() # 关闭文件

# f = open("aaa.txt",'r')
#
# # print(f.read()) # 默认读取全部数据
# # print(f.read(10)) # 读取指定大小的数据
# # print(f.readline()) # 按行读取，读取一行
# print(f.readlines()) # 按行读取，读取所有行
# f.close()


