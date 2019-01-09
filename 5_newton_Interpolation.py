#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/6 10:38
# @Desc      : 用牛顿插值法拟合经过给定点的曲线

#  x0 | y0
#  x1 | y1  y10
#  x2 | y2  y21   y210

import matplotlib.pyplot as plt
import numpy as np


def newton_interpolate(x, y):
    """
    :param x: 点集的x坐标集x[]
    :param y: 点集的y坐标集y[]
    :return: 拟合出的曲线系数列表coe[]
    """

    n = len(x)
    mat = np.zeros((n, n), dtype=float)

    # 将矩阵的第一列元素分别赋值为y[i]
    for i in range(n):
        mat[i][0] = y[i]

    for i in range(1, n):  # 对于第1~n-1列
        for j in range(i, n):  # 每列从上到下填入各差商值，即从三角形的斜边到直角边
            mat[j][i] = (mat[j][i - 1] - mat[j - 1][i - 1]) / (x[j] - x[j - i])

    # 输出对角线系数
    coe = []
    for i in range(n):
        coe.append(mat[i][i])

    return coe


def draw(x, y, coe):
    # 画图
    plt.title("Newton Interpolation")
    plt.scatter(x, y, label="discrete data", color='green')
    ltx = np.linspace(-5, 5, 300)
    lty = [coe[0] + coe[1] * (xi - x[0]) + coe[2] * (xi - x[0]) * (xi - x[1])
           + coe[3] * (xi - x[0]) * (xi - x[1]) * (xi - x[2])
           for xi in ltx]
    plt.plot(ltx, lty, label="fitting curve", color='red')
    plt.legend(loc="upper right")
    plt.show()


if __name__ == '__main__':
    # 设置拟合数据,求三次牛顿多项式
    x = [3, 2, -1, -2]
    y = [-23, -4, 5, 12]
    coe = newton_interpolate(x, y)
    print("拟合曲线的系数(b0~bn-1)：\n", coe)
    draw(x, y, coe)
