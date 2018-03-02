# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/2 16:22'

"""
设计一个算法，计算出n阶乘中尾部零的个数
样例
11! = 39916800，因此应该返回 2
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """

    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        i = 5
        while n / i > 0:
            count += int(n / i)
            i = i * 5
        return count


S = Solution()
print(S.trailingZeros(105))
