# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/23 21:18'

"""
二分查找
"""


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        value = list[mid]
        if value == item:
            return mid
        elif value > item:
            high = mid - 1
        elif value < item:
            low = mid + 1
    return None


mylist = [1, 3, 5, 7, 9]
print(binary_search(mylist, 3))