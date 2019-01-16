#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/26 11:43
# @Desc      : 使用LU分解法求线性方程组的解，同时使用PA=LU法进行精简


import numpy as np


def get_LUP(a):
    """
    获取分解的LU三角矩阵，保存列主元置换的矩阵P
    :param a:方程组的系数矩阵
    :return:列表LU[L, U, P]
    """

    n = len(a)
    L = np.zeros((n, n))
    P = np.zeros((n, n))
    # 初始化L与P为单位矩阵
    for i in range(n):
        L[i][i] = 1
        P[i][i] = 1

    for i in range(n):
        # 交换主元
        max = abs(a[i][i])
        index = i
        for m in range(i + 1, n):
            if abs(a[m][i]) > max:
                max = abs(a[m][i])
                index = m
        if max == 0:  # 奇异
            print("为奇异方程组，无解！")
            return None
        elif index != i:
            # 记录交换（因为P初始为单位矩阵，所以仅交换值为1的元素即可）
            P[i][i], P[index][i] = P[index][i], P[i][i]
            P[index][index], P[i][index] = P[i][index], P[index][index]
            # 交换行
            for m in range(i, n):
                a[i][m], a[index][m] = a[index][m], a[i][m]
        # 消去
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            L[j][i] = factor
            for k in range(i + 1, n):
                a[j][k] -= factor * a[i][k]

    LUP = [L, a, P]
    return LUP


def get_x(L, U, P, b):
    """
    求方程的解集
    :param L: 下三角L矩阵
    :param U: 上三角U矩阵
    :param P: 置换矩阵
    :param b: 方程组的常数项一维数组
    :return: 线性方程组的解集数组ans
    """
    n = len(b)

    # 置换b (b1 = Pb)
    b1 = np.zeros(n)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += P[i][j] * b[j]
        b1[i] = sum

    # 自顶向下回代求解D (LD = b1)
    D = np.zeros(n)
    D[0] = b1[0]
    for i in range(1, n):
        D[i] = b1[i]
        for j in range(i):
            D[i] -= L[i][j] * D[j]

    # 自底向上求解x (Ux = D)
    ans = np.zeros(n)
    ans[n - 1] = D[n - 1] / U[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        sum = D[i]
        for j in range(i + 1, n):
            sum -= ans[j] * U[i][j]
        ans[i] = sum / U[i][i]

    return ans


if __name__ == '__main__':
    # 输入测试用例
    n = int(input("请输入方程组未知量的个数："))
    print("请依次输入方程组的系数：")
    a = np.zeros((n, n))
    for i in range(n):
        line = input("第%d行：" % i).split()  # 默认以空格为分割
        for j in range(n):
            a[i][j] = float(line[j])

    print("\n请依次输入方程组的常数：", end="")
    b = np.zeros(n)
    line = input().split()
    for j in range(n):
        b[j] = float(line[j])

    LUP = get_LUP(a)
    if LUP is not None:
        print("求解答案：\n", get_x(LUP[0], LUP[1], LUP[2], b))
