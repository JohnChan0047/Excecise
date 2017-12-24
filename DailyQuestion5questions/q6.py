# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/23 21:08'
"""
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

使用Step-wise线性搜索。
"""


def get_value(l, r, c):
    return l[r][c]


def find(l, x):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n
    while r <= m and c >= 0:
        value = get_value(l, r, c)
        if value == x:
            return True
        elif value > x:
            c -= 1
        elif value < x:
            r += 1
