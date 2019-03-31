# -*- coding: utf-8 -*-
import math


class Sphere(object):
    """圆"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * pow(self.radius, 2)

    @property
    def volume(self):
        return 4 * math.pi * pow(self.radius, 3) / 3


def main():
    radius = input("请输入半径：")
    while True:
        try:
            radius = float(radius)
            break
        except ValueError:
            radius = input("输入错误，请重新输入半径：")
    sphere = Sphere(radius)
    print(sphere.diameter, sphere.circumference, sphere.area, sphere.volume)


if __name__ == '__main__':
    main()
