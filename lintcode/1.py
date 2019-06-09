# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/1 23:55'

"""
给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        return sum([a, b])


S = Solution()
print(S.aplusb(2, 3))
