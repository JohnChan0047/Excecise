# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 13:41'


class URL():
    def __init__(self, scheme, netloc, path, query_params, fragment):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.query_params = query_params
        self.fragment = fragment


def url_parse(url):
    scheme = url.split('://')[0]
    netloc = url.split('://')[1].split('/')[0]
    path = '/'+url.split('://')[1].split('/')[1].split('?')[0]
    temporary = url.split('://')[1].split('/')[1].split('?')[1].split('#')[0].split('&')
    query_params = {}
    for tem in temporary:
        if tem.count('=') != 1:
            tem_list = tem.split('=')
            for i in range(len(tem_list)):
                if tem_list[i] == '':
                    tem_list[i] = '='
            st = ''
            for i in tem_list[1:]:
                st = st + i
                query_params[tem_list[0]] = st
        else:
            tem_list = tem.split('=')
            query_params[tem_list[0]] = tem_list[1]
    fragment = url.split('://')[1].split('/')[1].split('?')[1].split('#')[1]
    return URL(scheme, netloc, path, query_params, fragment)


url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
URL = url_parse(url)
print(URL.scheme)
print(URL.netloc)
print(URL.path)
print(URL.query_params)
print(URL.fragment)