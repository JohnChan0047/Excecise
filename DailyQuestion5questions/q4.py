# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 12:59'

"""
## 第4题：

用Python实现斐波那契数列，费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出，
例如前 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。用数学方法可定义为如图所示：
"""

f_list = [0, 1]


def func(n):
    while n > len(f_list):
        f_list.append(f_list[-1] + f_list[-2])
    return f_list[n-1]


print(func(1))
print(func(2))
print(func(3))
print(func(4))
print(func(5))