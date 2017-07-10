# Problem 7
# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# 第10001个素数
# 列出前6个素数，它们分别是2、3、5、7、11和13。我们可以看出，第6个素数是13。
#
# 第10,001个素数是多少？
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
li = []
a = 1
while len(li)<10001:
    if func(a):
        li.append(a)
    a = a+1
print(li)
print(len(li))
print(li[-1])