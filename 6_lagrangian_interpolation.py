#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/7 22:17
# @Desc      : 用拉格朗日插值法拟合经过给定点的曲线


import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, lambdify


def lagrangian_interpolate(ltx, lty):
    """
    :param x: 点集的x坐标集x[]
    :param y: 点集的y坐标集y[]
    :return: 拉格朗日多项式Lx
    """

    x = symbols('x')
    lag = 0
    n = len(ltx)

    for i in range(n):  # 求 L(x) = ∑ l_i(x)*y_i
        t = 1
        for j in range(n):  # 求 l_i(x) = ∏ (x-x_j)/(x_i - x_j)
            if i != j:
                t *= (x - ltx[j]) / (ltx[i] - ltx[j])
        lag += t * lty[i]
    print("过所给点的拉格朗日多项式为：\nL(x) = ", lag)
    Lag = lambdify(x, lag)
    return Lag


def draw(x, y, Lag):
    # 画图
    plt.title("Lagrangian Interpolation")
    plt.scatter(x, y, label="discrete data", color='green')
    ltx = np.linspace(-5, 5, 300)
    lty = [Lag(i) for i in ltx]
    plt.plot(ltx, lty, label="fitting curve", color='red')
    plt.legend(loc="upper right")
    plt.show()


if __name__ == '__main__':
    # 设置拟合数据,求拉格朗日多项式
    x = [3, 2, -1]
    y = [-23, -4, 5]
    Lag = lagrangian_interpolate(x, y)
    draw(x, y, Lag)
