#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/18 0:40
# @Desc      : 利用二次样条法拟合经过给定点的曲线


import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve


def spline(lt):
    """
    :param lt: 含有给定点集合的列表[(x,y)...]
    :return: 各个样条虚线的系数列表coe[a,b,c....]
    """

    # 将点集列表按x的大小升序排
    lt.sort(key=lambda x: x[0])

    n = len(lt) - 1  # 样条个数
    num = n * 3  # 未知量的总数

    # 初始化系数方程组矩阵
    X = np.zeros((num, num))
    Y = np.zeros(num)
    b = 0
    j = 0
    k = 0
    # 每个样条过两个已知点
    for i in range(2 * n):
        yNum = lt[j][1]
        xNum = lt[j][0]
        number = 3 * k
        Y[i] = yNum
        X[i][number] = xNum ** 2
        X[i][number + 1] = xNum
        X[i][number + 2] = 1
        if b == 0:
            b = 1
            j += 1
        elif b == 1:
            b = 0
            k += 1
    k = 0
    j = 1
    #  相邻样条在内部节点处的一阶导数相等
    for i in range(2 * n, num - 1, 1):
        number1 = 3 * k
        number2 = 3 * (k + 1)
        X[i][number1] = 2 * lt[j][0]
        X[i][number1 + 1] = 1
        X[i][number2] = -2 * lt[j][0]
        X[i][number2 + 1] = -1
        j += 1
        k += 1
    # 设置a0 = 0
    X[num - 1][0] = 1
    # 求解方程组
    coe = solve(X, Y)
    return coe


def draw(lt, coe):
    """
    画图
    :param lt: 含有给定点集合的列表[(x,y)...]
    :param coe: 各个样条虚线的系数列表[a,b,c....]
    """
    lt.sort(key=lambda x: x[0])
    func = lambda a, b, c, x: a * (x ** 2) + b * x + c
    n = len(lt) - 1
    plt.title("Spline Interpolation")
    for i in range(n):
        x1 = lt[i][0]
        x2 = lt[i + 1][0]
        ltx = np.arange(x1, x2 + 0.01, 0.01)
        index = i * 3
        a = coe[index]
        b = coe[index + 1]
        c = coe[index + 2]
        # 画点和线
        plt.scatter(lt[i][0], lt[i][1], color='green')
        plt.plot(ltx, func(a, b, c, ltx), color='red')

    plt.scatter(lt[n][0], lt[n][1], color='green')
    plt.show()


if __name__ == '__main__':
    # 设置拟合点
    lt = [(3, -23), (2, -4), (-1, 5), (-2, 12)]
    coe = spline(lt)
    draw(lt, coe)
