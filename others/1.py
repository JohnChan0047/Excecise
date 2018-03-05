# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/4 16:23'

"""
写一个函数分割一个整数数组，使得奇数在前偶数在后。

挑战：

在原数组中完成，不使用额外空间。

格式：

输入行输入一个整数数组，最后输出分割后的数组。

[ 1， 2，3，4 ]
"""


def func(L):
    n = len(L)
    low = 0
    height = n -1
    while low < height:
        if L[low] % 2 != 0:
            low += 1
        if L[height] % 2 == 0:
            height -= 1
        if low > height:
            break
        else:
            L[low], L[height] = L[height], L[low]
    return L


print(func([1, 2, 3, 4, 5, 6, 7, 8]))
