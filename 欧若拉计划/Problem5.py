# Problem 5
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# 最小倍数
# 2520是最小的能够被1到10整除的数。
#
# 最小的能够被1到20整除的正数是多少？
#
from time import ctime
print(ctime())
n = 1
x = 20
i = 1
while i <= 20:
    if x % i == 0:
        i = i + 1
        continue
    else:
        i = 1
        n = n + 1
        x = 20 * n
print(x)
print(ctime())
# Sun Jul  9 13:26:55 2017
# 232792560
# Sun Jul  9 13:27:05 2017
# 用了约11秒。