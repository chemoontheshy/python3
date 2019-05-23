def hello():
    print("hello world!")


hello()


# 带参数的函数
def area(width, helght):
    return width * helght


def welcome(name):
    print("Welcome", name)


welcome("chenmo")

w = 3

h = 4
print("width=", w, "height=", h, "area=", area(w, h))


# 不定长参数
# 加入*的参数会以元组（tuple）的形式导入，存放所有未命名的变量参数
def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print("输出：")
    print(arg1)
    print(vartuple)


printinfo(60, 30, 34)


# 加入**的参数会以字典（dict）的形式导入。

def printinfo(arg1, **vardict):
    """打印任何传入的参数"""
    print("输出：")
    print(arg1)
    print(vardict)


printinfo(1, a=2, b=3)

# lambda:匿名函数

sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))


# return语句
# return[表达式]语句用于退出函数，选择性地向调用方返回一个表达式，不带参数值的return语句返回none。
def sum(arg1, arg2):
    # 返回2个参数的和。#
    total = arg1 + arg2
    print("函数内：", total)
    return total


total = sum(10, 20)
print("函数外：", total)
