# -*- coding: utf-8 -*-


def distance(initial_height, time, ratio=0.6):
    """
    物体下落总距离
    :param initial_height: 初始高度
    :param time: 统计持续弹跳次数
    :param ratio: 反弹比率
    :return: 总距离
    """
    total = 0
    while time:
        total = total + initial_height + initial_height * ratio
        initial_height = initial_height * ratio
        time -= 1
    return total


if __name__ == '__main__':
    while True:
        try:
            initial_height = float(input("输入初始高度："))
            time = float(input("输入统计次数："))
            break
        except ValueError:
            print("请输入数字！")
    print("总距离为：{}".format(distance(initial_height, time)))
