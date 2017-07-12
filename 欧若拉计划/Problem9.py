
# Problem 9
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.
#
# 特殊毕达哥拉斯三元组
# 毕达哥拉斯三元组是三个自然数a < b < c组成的集合，并满足
#
# a**2 + b**2 = c**2
# 例如，3**2 + 4**2 = 9 + 16 = 25 = 52。
#
# 有且只有一个毕达哥拉斯三元组满足 a + b + c = 1000。求这个三元组的乘积abc。
# n = 10
# while n < 1000:
# 	for x in range(1, n):
# 		for y in range(x, n):
# 			for z in range(y, n):
# 				if x**2 + y**2 == z**2 and x + y + z == 1000:
# 					print(x,y,z)
# 		n +=1
# 应当缩小循环的范围
# 根据勾股定理
t = False
for x in range(1, 293):
	for z in range(x+1, 500):
		y = 1000-x-z
		if z**2 == x**2 + y**2:
			t = True
			print('%d * %d * %d = %d' % (x, y, z, x*y*z))
			break
	if t:
		break