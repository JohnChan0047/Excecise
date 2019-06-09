# -*- coding: utf-8 -*-
source_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]


def search(target, source):
    left = 0
    right = len(source) - 1
    while left <= right:
        middle = (right + left) // 2
        print(source[left], source[middle], source[right])
        if source[middle] == target:
            return source[middle]
        elif source[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return None


print(search(90, source_list))
print(search(44, source_list))
