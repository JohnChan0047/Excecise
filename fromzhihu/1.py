# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/13 15:25'
"""
写一个函数，输入 lst = [1, 1, 3, 4, 4, 1]，返回值为[1,3,4,1]。

需求是：如果后一个数字与前一个数字相同，则只保留一个数。
"""
L = []
while True:
    n = input('请输入数字，输入q结束：')
    if n == 'q' or type(n) != int:
        break
    else:
        if n in L:
            continue
        else:
            L.append(n)
print(L)