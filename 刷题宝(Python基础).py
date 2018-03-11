# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/7 21:35'
import string
import random
import os
import re
import copy
import socket

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
print(string.printable)
print(2 * 'work')
print(2 ** (-2))
a = '{:>10s}{:>10s}'.format('hello', 'world')
print(a, len(a))
print(random.sample(range(100, 200), 10))
#
#


def datetimeFormat(func):
    def wrap(*args, **kwargs):
        print(args[0])
        return func(*args,**kwargs)
    return wrap


@datetimeFormat
def day_period(enddate,period,*args,**kwargs):
    pass


day_period('20160101', 7)
#
#
print(os.getcwd())
fpath, fname = os.path.split("C:\\Users\\test.txt")
print(fpath, fname)
dic = {'name': 'John', 'age': 23}
print(dic.keys())
p = re.compile('ab*', re.I)  # 忽略大小写，取短
print(p.findall('abAB'))
p = re.compile('\^ab')
print(p.findall('^abAB  ^abc ccc ABc'))
a = [1, 2, 3, ['a', 'b', 'c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(
    id(a) == id(c),
    id(a) == id(d),
    id(a[0]) == id(c[0]),
    id(a[3]) == id(d[3]),
)
a.append(5)
a[0] = 2
# a[3].append(1)
print([id(ele) for ele in a])
print([id(ele) for ele in b])
print([id(ele) for ele in c])
print([id(ele) for ele in d])
print(socket.gethostname())

#
#
import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print(self.isDaemon())


if __name__ == "__main__":
    t = MyThread()
    t.start()
#
print('b' and 'a')
print('b' or 'a')
a = [1, 2, 3]
b = [4, 5, 6]
for (a_val, b_val) in zip(a, b):
    print(a_val, b_val)

f0, f1, f2 = [lambda x: x*i for i in range(3)]
f3, f4, f5 = [lambda x: x*0, lambda x: x*1, lambda x: x*2]
print(f0(1))
print(f1(1))
print(f2(1))
print(f3(1))
print(f4(1))
print(f5(1))
f = [lambda x: x*i for i in range(3)]
print(type(f))
print(sum(map(lambda x: -1, (5,)*9))^0)
print((5, )*9)
print((-1) ^ 0)
print([i for i in map(lambda x: -1, (5, )*9)])
