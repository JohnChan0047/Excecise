# -*- coding: utf-8 -*-


def get_pi(time):
    """
    近似求pi
    :param time: 统计次数
    :return: pi
    """
    denominators = [2 * number + 1 for number in range(time)]
    return 4 * sum([((-1) ** index) / number for index, number in enumerate(denominators)])


if __name__ == '__main__':
    while True:
        try:
            time = int(input(u"输入迭代次数："))
            if time > 0:
                break
            print("请输入正整数")
        except ValueError:
            print("请输入正整数")
    print("pi: {}".format(get_pi(time)))
