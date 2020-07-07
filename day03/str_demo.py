# a = "123"
# b = "456"
#
# print(a + b)
# print(a)
# print(b)




# a = "abcdefghijklmn"
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])

# a = "abcdefghijklmn"
# for i in a:
#     print(i)
#
# s = "   aassss   "
#
# print(s.strip())
# print(s.lstrip())
# print(s.lstrip())

# l = "safdsf,sdfsdf,gggg"
# print(l.split(","))
#
# with open("aaa.txt",'r') as f: # with 使用一个上下文管理器
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""),end="") # print 默认带一个换行

#
#
# s = "sdjfisjif.sfjisjdfi"
#
# print(s.find(".sf"))
# # 通过占位符格式化
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%d X %d = %d"%(j,i,i*j), end="\t")
#     print()
#
# # .format
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{} X {} = {}".format(j,i,i*j), end="\t")
#     print()
#
#
#
# print("{:,}".format(10000000000000))
#
# print("{:0>10}".format(123))
#
# print("{:.3f}".format(2.3467698781))



# l = [1,23,2,4,6,7,87]
#
# l[0] = 20
# print(l)
# l[1:3] = 20,30
# print(l)
# l = [2,3,4,5]
# # l.append("王大锤")
# # l.append("王大锤")
# # l.extend({'123',123})
# l.insert(1,"王大吃哦")
# print(l)
#
#
# print(l.pop())
# print(l)
#
# print(l.pop(1))
# print(l)
#
# l.remove(3)
# print(l)
#
#
# l = [2,34,2,5,7,8,2]
# l.remove(2)
# print(l)
#
# l = [True,1,2,5,7,8,2]# python True 1 false 0
# l.remove(1)
# print(l)
#
# l.clear()
# print(l)

# a = [5,2,3,6,8,9,123,3,5,7,8123,4]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# d = {"name":"小明","age":18,"sex":"男"}
#
# for key in d:
#     print(d[key])
#
# for k,v in d.items():
#     print(k,v)

# d["addr"] = "上海闵行"
# print(d)
# d["addr"] = "上海浦东"
# print(d)

# d = {"name":"小明","age":18,"sex":"男"}
#
#
# d.update({"addr":"上海闵行","学历":"本科"})
# print(d)
#
# print(d.pop("addr"))
# print(d)
#
# s = {}
# for key in d:
#     if key.startswith("a"):
#         continue
#     s[key] = d[key]
# print(s)

#
# # 语法检查
# a = 100
# print(b) # 语法错误
# b= 20 # 语法错误

# f = open("bbbb.txt", 'r')  # 异常
# print(f.read())
# f.close()
#
# try:
#     f = open("bbbb.txt",'r')  # 异常
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
#
# print("操作完文件")




# def div(a,b):
#     try:
#         print(a / b)
#     except ZeroDivisionError as e:
#         print(e)
#     else:
#         print("除法执行成功")
#     finally:
#         print("不管try中是否报错，都会被执行")
#
#
# div(10,0)


class CustomException(Exception):
    def __init__(self,value="值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 0
try:
    if a == 0 :
        print("a = {} 触发异常".format(a))
        raise CustomException
    print("a= {} 未触发异常".format(a))
except CustomException as e:
    print(e)


