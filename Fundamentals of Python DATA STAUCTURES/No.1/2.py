# -*- coding: utf-8 -*-


def weekly_pay(hour_pay, routine_hours, out_time):
    """
    雇员周薪
    :param hour_pay: 日薪
    :param routine_hours: 每周常规工作时间
    :param out_time: 加班时间
    :return: 周薪
    """
    return hour_pay * routine_hours + 1.5 * hour_pay * out_time


if __name__ == '__main__':
    hour_pay, routin_hours, out_time = 0, 0, 0
    while True:
        try:
            hour_pay = float(input("请输入日新："))
            routin_hours = float(input("请输入每周常规工作时间："))
            out_time = float(input("请输入每周加班时间: "))
            break
        except ValueError:
            print("输入出错，请输入数字！")

    print("周薪：{}".format(weekly_pay(hour_pay, routin_hours, out_time)))
