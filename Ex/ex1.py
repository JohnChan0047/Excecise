# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
li = [1, 2, 3, 4]
x_list = []
for b in li:
    for s in li:
        for g in li:
            if b != s and b != g and s != g:
                x = b*100 + s*10 + g
                x_list.append(x)
print(x_list)
