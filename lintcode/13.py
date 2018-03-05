# -*- coding:utf-8 -*- 
__author__ = 'John 2018/3/5 15:19'


"""
对于一个给定的 source 字符串和一个 target 字符串，
你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
样例
如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。
"""


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if target == '':
            return 0
        else:
            if target in source:
                for n, i in enumerate(source):
                    if i == target[0]:
                        return n
            else:
                return -1


S = Solution()

