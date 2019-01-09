#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018‎/11‎/19 ‎‏‎22:03
# @Desc      : 使用二分法(bisection method)求解方程的近似根

from sympy import symbols, lambdify, plot


def bisecrt():
    x = symbols('x')
    f = x ** 3 + x - 1
    func = lambdify(x, f)
    a = -1
    b = 1
    tol = 0.000001

    xc = (a + b) / 2
    while b - a > tol:
        f_xc = func(xc)
        if f_xc == 0:
            break
        else:
            f_a = func(a)
            if (f_a * f_xc) < 0:
                b = xc
            else:
                a = xc
        xc = (a + b) / 2

    print("方程[ %s = 0 ]在误差范围为(%f)的近似解为x = %f" % (f, tol, xc))
    plot(f, (x, -1, 1))


if __name__ == '__main__':
    bisecrt()
