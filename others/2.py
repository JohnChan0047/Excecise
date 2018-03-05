# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/4 16:35'

"""
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序。写一个函数实现此功能。
"""


def func(L):
    n = len(L)
    t = 0
    for i in range(n):
        if L[i] == 0:
            L.remove(L[i])
            L.append(0)
            t += 1
        if t + i > n:
            break


L = [0, 1, 3, 5, 0, 12, 0, 1, 0]
func(L)
print(L)
