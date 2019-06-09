# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/2 17:31'

"""
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
样例
如果n = 9， 返回 10
"""


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        result = 0
        while n > 0:
            result += 1
            if self.IsUgly(result):
                n -= 1
        return result

    def IsUgly(self, n):
        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5
        if n == 1:
            return True


S = Solution()
print(S.nthUglyNumber(599))
