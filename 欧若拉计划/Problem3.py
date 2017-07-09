# Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# 最大质因数
# 13195的所有质因数为5、7、13和29。
#
# 600851475143最大的质因数是多少？

# 先求所有因数，在求质因数的方式会导致无法运算
# factor = []
# for n in range(1, 600851475144):
#     if 13195 % n == 0:
#         # print(n)
#         factor.append(n)
# print(factor)

# 任何正整数可以分解为质因数的幂的积
def fun(x):
    n = 2
    pf = []
    while n <= x:
        if x % n == 0:
            x = x / n
            if n not in pf:
                pf.append(n)
        else:
            n = n + 1
    return pf
prime_factor = fun(600851475144)
print(prime_factor)
print(prime_factor[-1])

