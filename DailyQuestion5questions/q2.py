# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 11:53'

"""
## 第2题：

设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，
每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。
"""

import random


number = random.randint(1, 100)
n = 5
flag = True
while n > 0 and flag:
    n -= 1
    play_number = int(input('请输入数字：'))
    if play_number == number:
        flag = False
    elif play_number > number:
        if n == 0:
            break
        else:
            print('输入数字偏大，请重新输入，还剩%s次机会。' % n)
    else:
        if n == 0:
            break
        else:
            print('输入数字偏小，请重新输入，还剩%s次机会。' % n)


if flag is not True:
    print('猜中了')
if n < 1:
    print('游戏结束，正确数字是%s。' % number)