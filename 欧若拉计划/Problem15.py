# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/13 9:52'
"""
网格路径
从一个2×2方阵的左上角出发，只允许向右或向下移动，则恰好有6条通往右下角的路径。


对于20×20方阵来说，这样的路径有多少条？
"""


def func(n):
    L = [1] * n
    for i in range(n):
        for j in range(i):
            L[j] = L[j] + L[j-1]
        L[i] = 2 * L[i-1]
    return L[n-1]


print(func(20))