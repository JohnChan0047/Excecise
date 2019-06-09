# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/1 23:15'

"""
给出两个数 A 和 B, 其中 B >= A. 我们需要计算结果 F 的最后一位数是什么, 其中F = B! / A!(1 <= A, B <= 10^18, A 和 B 非常大)

给出 A = 2, B = 4, 返回 2
A! = 2 以及 B! = 24, F = 24 / 2 = 12 --> 最后一位数为 2 

给出 A = 107, B = 109, 返回 2
"""


class Solution:
    """
    @param A: the given number
    @param B: another number
    @return: the last digit of B! / A!
    """

    def computeLastDigit(self, A, B):
        # write your code here
        if B - A > 10:
            return 0
        else:
            s = 1
            for i in range(A + 1, B + 1):
                s = s * i
            return s % 10


S = Solution()
print(S.computeLastDigit(2, 4))
print(S.computeLastDigit(234300352440211300, 829691773056400707))
