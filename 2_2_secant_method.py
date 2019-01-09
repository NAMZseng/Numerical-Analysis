#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/11/22 22:40
# @Desc      : 使用正割法求解函数f(x)=x^2-10x = 0的近似解


import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x ** 2 - 10 * x


def newton(x1, x0, tol, max):
    """
    :param x0, x1:割线上的初始点
    :param tol: 容差
    :param max: 最大迭代次数
    :return: [近似点,迭代次数]
    """
    k = 0
    while k < max:
        xi = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))
        if abs(xi - x1) < tol:
            return [xi, k]
        else:
            x0 = x1
            x1 = xi
            k += 1

    if k == max:
        return None


if __name__ == '__main__':
    ans = newton(-8, -9, 0.0001, 1000)
    if ans is None:
        print("迭代失败")
    else:
        # 打印图像
        x = np.linspace(-15, 5, 200)
        g = [f(i) for i in x]

        plt.plot(x, g)
        plt.scatter(ans[0], f(ans[0]), s=66, color='b')
        plt.annotate(r'$%f$' % ans[0], xy=(ans[0], f(ans[0])), xycoords='data', xytext=(-30, +30),
                     textcoords='offset points', fontsize=16)
        plt.text(-5, 300, r'$Iteration\ Times:\ %d$' % ans[1], fontdict={'size': 16})
        plt.show()
