# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/7 21:35'
import string

print(set([1, 2]))  # {1，2}
print((2))  # 2
print((2,))  # （2，）
print("g".center(5, "o"))  # 'oogoo'
print("google".count("o", 0, 2))  # 1
print("Usa13".isalnum())  # True 判断是否字母或数字
print("".isspace())  # False 判断是否空格
print(','.join(['a', 'b']))  # 'a,b'
print('www.example.com'.lstrip('cmowz.'))  # 'example.com'
print('aBc'.swapcase())  # 'AbC'
print('5'.zfill(10))  # 0000000005字符串前添加0
print(string.digits)

#
a = 1


def do_something():
    global a  # 在函数内部给全局变量赋值
    a = 2


do_something()
print(a)
#


#
def minus(a, b):
    x = a - b


print(minus(b=5, a=4))
#


#
params1 = (8, 9)
params2 = {"a": 4, "b": 5}


def minus(a, b):
    return a - b


print("%d,%d" % (minus(*params1), minus(**params2)))
#


#
class A(object):
    attr = 4


class B(A):
    def __init__(self, b):
        self.x = b


class C(B):
    x = 6


print(C(9).x)
#


# 静态方法
class Ball(object):

    def __init__(self, name):
        self.name = name

    @staticmethod
    def func(x, y):
        return x * y


print(Ball.func(2, 6))
#


#


class Go:
    name = 'hello'


def toupper(self):
    return self.name.upper()


print(toupper(Go()))
print(type(toupper(Go())))
#
a = [1, 2, 3, 4, 5, 6]
b = a[1:4]
print(b)
#
#
print("%05.2f" % 1.111)
#
#
aList = [1, 3, 5, 2, 4]
aList = aList.sort()  # sort()没有返回值
print(aList)
#
#
print((5).bit_length())  # 转为二进制后求位数
#
#
print(u"hello world")
#
#
num = '四'
print(num.isnumeric())
#
#
mylist = [1, 2, 3, 4]
mylist.sort(reverse=True)
print(mylist)
#
#
exec('print("love")')
#
#
print(string.printable)
#