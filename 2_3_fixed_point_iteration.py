#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/11/22 23:32
# @Desc      : 使用简单定点迭代法求解函数f(x)=x^2-10x = 0的近似解


import matplotlib.pyplot as plt
import numpy as np

gx = lambda x: (x ** 2) / 10


def fbi(x0, tol, max):
    """
    :param x0: 迭代初值
    :param tol: 容差
    :param max: 最大迭代次数
    :return: [近似点,迭代次数]
    """
    k = 0
    while k < max:
        x1 = gx(x0)
        # 若g(x) = x,找到不动点
        if abs(x1 - x0) < tol:
            return [x1, k]
        else:
            x0 = x1
            k += 1

    if k == max:
        return None


if __name__ == '__main__':
    ans = fbi(-9, 0.0001, 1000)
    if ans is None:
        print("迭代失败")
    else:
        # 打印图像
        plt.title("fixed_point_iteration")
        x = np.linspace(-15, 5, 200)
        f = x
        g = [gx(i) for i in x]
        plt.plot(x, g)
        plt.plot(x, f, color='red', linestyle='--')

        plt.scatter(ans[0], ans[0], s=66, color='b')
        plt.annotate(r'$%f$' % ans[0], xy=(ans[0], ans[0]), xycoords='data', xytext=(0, -30),
                     textcoords='offset points', fontsize=16)
        plt.text(-7.5, 15, r'$Iteration\ Times:\ %d$' % ans[1], fontdict={'size': 16})
        plt.show()
