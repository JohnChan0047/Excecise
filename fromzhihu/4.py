# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/14 9:48'
"""
元音字母 有：a，e，i，o，u五个， 写一个函数，交换字符串的元音字符位置。

假设，一个字符串中只有二个不同的元音字符。

二个测试用例：

输入 apple 输出 eppla

输入machin 输出 michan
"""


def reverse_vowel(s):
    s = list(s)
    L = ['a', 'e', 'i', 'o', 'u']
    F = [i for i in range(len(s)) if s[i] in L]
    s[F[0]], s[F[1]] = s[F[1]], s[F[0]]
    return ''.join(s)


print(reverse_vowel('apple'))
