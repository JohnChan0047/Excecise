# -*- coding:utf-8 -*- 
__author__ = 'John 2017/11/8 15:59'
"""
归并排序

归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

    自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）；
    自下而上的迭代；
    
2. 算法步骤

申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；

设定两个指针，最初位置分别为两个已经排序序列的起始位置；

比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；

重复步骤 3 直到某一指针达到序列尾；

将另一序列剩下的所有元素直接复制到合并序列尾。"""
import random
random_list = []
for i in range(20):
    random_list.append(random.randint(0, 20))
print(random_list)


def merge_sort(arr):
    if len(arr)<2:
        return arr
    middle = int(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(a, b):
    result = []
    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    while a:
        result.append(a.pop(0))
    while b:
        result.append(b.pop(0))
    return result


print(merge_sort(random_list))