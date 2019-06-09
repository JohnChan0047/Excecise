# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/5 15:30'

"""
给定一个数字列表，返回其所有可能的排列。
"""


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def func(self, nums):
        # write your code here
        result = []
        if nums is None:
            return result
        if len(nums) == 0:
            result.append([])
        for x in nums:
            temp_nums = nums[:]
            temp_nums.remove(x)
            for y in self.func(temp_nums):
                y.insert(0, x)
                result.append(y)
        return result


s = Solution()
print(s.func([2, 2, 1, 1]))
