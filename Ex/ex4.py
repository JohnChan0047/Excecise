# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
p = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
# r = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
data = input("输入日期，格式为'20170709'：")
year = int(data[:4])
month = int(data[4:6])
day = int(data[6:8])
if month > 12 or day > 31:
    print("日期输入错误")
else:
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        if month > 2:
            d = day + p[month-1] + 1
        else:
            d = day + p[month-1]
    else:
        d = day + p[month - 1]
    print(year, month, day)
    print(d)