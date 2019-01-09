#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2019/1/8 20:44
# @Desc      : 使用修恩法(Henu)近似求解常微分方程(ordinary differential equation)


import matplotlib.pyplot as plt
import numpy as np


def heun(D, p0, left, right, n):
    """
    修恩法
    :param D: 常微分方程的lamda表达式
    :param p0: 初始点元组
    :param left: 区间左边界
    :param right: 区间右边界
    :param n: 求解点的个数
    :return: 求得的方程点集ltH[(x, y)]
    """

    h = (right - left) / n
    ltH = []
    x0 = p0[0]
    y0 = p0[1]
    for i in range(n):
        k1 = D(x0)
        x0 += h
        k2 = D(x0)
        y0 += h * (k1 + k2) / 2
        ltH.append((x0, y0))

    return ltH


def draw(F, ltH, left, right):
    """
    画正解的函数图和通过修恩法求得的函数图
    :param F: 表示正解函数方程的lamda表达式
    :param ltH: 修恩法求得的解集
    :param left: 区间左边界
    :param right: 区间右边界
    """
    plt.title("Heun_Method")

    # 画正解函数图像
    f_x = np.linspace(left, right, 100)
    f_y = [F(xi) for xi in f_x]
    plt.plot(f_x, f_y, color='green', label="currect curve")

    # 画修恩法图像
    h_x = [ltH[i][0] for i in range(len(ltH))]
    h_y = [ltH[i][1] for i in range(len(ltH))]
    plt.scatter(h_x, h_y, color='blue', label="Heun point")
    plt.plot(h_x, h_y, color='red', label="Heun curve")
    plt.legend(loc="upper left")
    plt.show()


if __name__ == '__main__':
    # 测试PPT范例
    D = lambda x: -2.0 * x ** 3 + 12 * x ** 2 - 20 * x + 8.5
    F = lambda x: -0.5 * x ** 4 + 4 * x ** 3 - 10 * x ** 2 + 8.5 * x + 1
    ltH = heun(D, (0, 1), 0, 4, 8)
    draw(F, ltH, 0, 4)
