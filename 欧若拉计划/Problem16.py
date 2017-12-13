# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/13 10:40'
"""
幂的数字和
215 = 32768，而32768的各位数字之和是 3 + 2 + 7 + 6 + 8 = 26。

21000的各位数字之和是多少？
"""
n = 2**1000
sum = 0
for i in str(n):
    sum = sum + int(i)
print(sum)