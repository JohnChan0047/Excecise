# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/1 22:40'

"""
给一个数字 n, 以字符串的形式返回数字的阶乘
给一个数字 n = 20
返回 2432902008176640000
"""


class Solution:
    """
    @param n: an integer
    @return:  the factorial of n
    """
    def factorial(self, n):
        # write your code here
        result = 1
        for i in range(1, n+1):
            result = result * i
        return str(result)


S = Solution()
print(S.factorial(0))