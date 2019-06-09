# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
import time

a = [1, 2, 3]
for i in a:
    print(time.ctime())
    print(i)
    time.sleep(1)
    print(time.ctime())
