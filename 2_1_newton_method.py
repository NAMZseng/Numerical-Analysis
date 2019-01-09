#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/1/22 10:29
# @Desc      : 使用牛顿切线法求解函数f(x)=x^2-10x = 0的近似解


import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x ** 2 - 10 * x
df = lambda x: 2 * x - 10


def newton(x0, tol, max):
    """
    :param x0: 迭代初值
    :param tol: 容差
    :param max: 最大迭代次数
    :return: [近似点,迭代次数]
    """
    k = 0
    while k < max:
        if df(x0) == 0:
            return None
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return [x1, k]
        else:
            x0 = x1
            k += 1

    if k == max:
        return None


if __name__ == '__main__':
    ans = newton(-9, 0.0001, 1000)
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
