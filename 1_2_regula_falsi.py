#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/11/19 22:28
# @Desc      : 用试位法(regula falsi)求解方程的近似根


from sympy import symbols, lambdify, plot


def falsi():
    x = symbols('x')
    f = x ** 3 + x - 1
    func = lambdify(x, f)
    a = -1
    b = 1
    tol = 0.000001

    xc = (b * func(a) - a * func(b)) / (func(a) - func(b))
    while b - a > tol:
        f_xc = func(xc)
        if f_xc == 0:
            break
        else:
            f_a = func(a)
            f_b = func(b)
            if (f_a * f_xc) < 0:
                b = xc
            else:
                a = xc
        xc = (b * f_a - a * f_b) / (f_a - f_b)

    # 输出结果并打印函数图像
    print("方程[ %s = 0 ]在误差范围为(%f)的近似解为x = %f" % (f, tol, xc))
    plot(f, (x, -1, 1))


if __name__ == '__main__':
    falsi()
