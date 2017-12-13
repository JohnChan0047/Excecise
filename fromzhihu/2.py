# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/13 15:34'
"""
有一个json文件：

{"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]}, "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}}

现在要写一个函数search，当给search函数传入‘金字塔’的 时候，函数打印出奴隶社会.非洲.古埃及文明.
金字塔，当给search函数传入美洲的时候，打印出“不存在的关键字：美洲“
"""
import json

filename = '2.json'

with open(filename, 'r') as f:
    dic = json.load(f)

dic1 = {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]}, "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}


def search(dic, keywords):
    for k, v in dic.items():
        if k == keywords:
            print(k, v)
        elif isinstance(v, dict):
            search(v, keywords)
        elif keywords in v:
            print(k, v)


print(search(dic, keywords='金字塔'))

