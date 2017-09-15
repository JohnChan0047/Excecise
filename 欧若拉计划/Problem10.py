#
# Problem 10
# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# 素数的和
# 所有小于10的素数的和是2 + 3 + 5 + 7 = 17。
#
# 求所有小于两百万的素数的和。
def func(i):
    if i < 2:
        return False
    elif i == 2:
        return True
    elif i > 2:
        t = False
        for x in range(2, int(i**0.5)+1):# 减少时间
            if i % x == 0:
                t = True
                break
        if t:
            return False
        else:
            return True
n = 0
li = []
# while n < 2000000:
# 	if func(n):
# 		li.append(n)
# 	n += 1
# print(li)

for i in range(2000001):
	if func(i):
		li.append(i)
print(sum(li))