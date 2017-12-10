# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 12:12'

"""
## 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。
"""

with open('q3.txt', 'r') as f:
    text = f.read()

text = text.replace(',', '').replace('.', '').replace('\n', '')
words_list = text.split(' ')
removal_list = []
dic = {}
for i in words_list:
    if i not in removal_list:
        removal_list.append(i)
for i in removal_list:
    dic[i] = words_list.count(i)

lis = sorted(dic.items(), key=lambda d: d[1], reverse=True)
print(lis[0:5])


from collections import Counter

text = text.split()
top_words = Counter(text).most_common(5)
print(top_words)