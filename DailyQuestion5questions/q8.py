# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/23 21:59'
"""
快排
"""


def quicksort(list):
    if len(list) < 2:
        return list
    else:
        midpivot = list[0]
        lessbeforemidpivot = [i for i in list[1:] if i <= midpivot]
        biggerafterpivot = [i for i in list[1:] if i > midpivot]
        finallylist = quicksort(lessbeforemidpivot)+[midpivot]+quicksort(biggerafterpivot)
        return finallylist


print(quicksort([2, 4, 6, 7, 1, 2, 5]))