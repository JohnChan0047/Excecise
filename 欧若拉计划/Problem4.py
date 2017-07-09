#
# Problem 4
# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# 最大回文乘积
# 回文数就是从前往后和从后往前读都一样的数。由两个2位数相乘得到的最大回文乘积是 9009 = 91 × 99。
#
# 找出由两个3位数相乘得到的最大回文乘积。
palindromic = []
for i in range(100, 999):
    for j in range(100, 999):
        x = i * j
        x = str(x)
        if x == x[::-1]:# 字符串切片方法
            palindromic.append(int(x))
print(palindromic)
print(max(palindromic))
