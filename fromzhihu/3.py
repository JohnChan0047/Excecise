# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/13 21:30'
"""
乒乓序列从1开始计数，始终向上计数或倒数。在元素k处，如果k是7的倍数或包含数字7，方向将切换。乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和第28个要素。

1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

实现一个返回乒乓序列第n个元素的函数乒乓。
"""


def pingpong(n):
    num = 0
    add_num = 1
    for i in range(n):
        num = num + add_num
        if '7' in str(num) or num % 7 == 0:
            add_num = add_num * (-1)
    return num


print(pingpong(70))