# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/8 10:40'
"""
选择排序

选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。
唯一的好处可能就是不占用额外的内存空间了吧。

算法步骤

首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。
"""
import random
random_list = []
for i in range(20):
    random_list.append(random.randint(0, 20))
print(random_list)


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_set = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min_set = j
        arr[i], arr[min_set] = arr[min_set], arr[i]
    return arr
# def selectionSort(arr):
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[i]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr


print(selection_sort(random_list))