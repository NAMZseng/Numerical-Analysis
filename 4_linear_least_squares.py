#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/3 18:36
# @Desc      : 利用最小二乘法求解基本的直线拟合问题

import random
import matplotlib.pyplot as plt
import numpy as np


def get_a_b(coe_a, coe_b, coe_c):
    """
    求正则方程组的解,相应行列式:  a0 b0 | c0
                                a1 b1 | c1
    :param coe_a:系数[a0, a1]
    :param coe_b:系数[b0, b1]
    :param coe_c:常数[c0, c1]
    :return: list[a, b]
    """
    D0 = coe_a[0] * coe_b[1] - coe_a[1] * coe_b[0]
    Du = coe_c[0] * coe_b[1] - coe_c[1] * coe_b[0]
    Dv = coe_a[0] * coe_c[1] - coe_a[1] * coe_c[0]
    if D0 == 0:
        return None
    else:
        a = Du / D0
        b = Dv / D0
        return [a, b]


def linear_least_squares(lt_x, lt_y):
    """
    根据最小二乘法求解实验数据的拟合直线 y=bx+a
    :param lt_x: 数据点的x坐标集
    :param lt_y: 数据点的y坐标集
    :return: list[a, b]
    """
    # 求正则方程组的系数
    n = len(lt_x)
    coe_a = [n, 0]
    coe_b = [0, 0]
    coe_c = [0, 0]
    for i in range(n):
        coe_a[1] += lt_x[i]
        coe_b[1] += lt_x[i] ** 2
        coe_c[0] += lt_y[i]
        coe_c[1] += lt_x[i] * lt_y[i]
    coe_b[0] = coe_a[1]

    return get_a_b(coe_a, coe_b, coe_c)


def draw(x, y, ans):
    plt.scatter(x, y, color='green')
    ltx = np.linspace(-15, 15, 300)
    lty = [ans[1] * xi + ans[0] for xi in ltx]
    plt.plot(ltx, lty, color='r')
    plt.text(-15, 10, 'fitting line\ny=%.2fx+%.2f' % (ans[1], ans[0]), fontdict={'size': 16})
    plt.show()


if __name__ == '__main__':
    # 生成直线拟合的随机点
    x = list(range(-10, 10))
    y = [xi + round(random.uniform(-2, 2), 2) for xi in x]
    ans = linear_least_squares(x, y)

    if ans is None:
        print('求解失败！')
    else:
        draw(x, y, ans)
