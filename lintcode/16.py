# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/5 16:49'


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

    def permute(self, nums):
        l1 = self.func(nums)
        l2 = []
        for i in l1:
            if i not in l2:
                l2.append(i)
        return l2


s = Solution()
print(s.permute([2, 2, 1, 1]))