#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/26 8:55
# @Desc      : 使用高斯消去法求线性方程组的解，同时使用交换列主元法进行精简


import numpy as np


def switch_principal(a, b, k):
    """
    交换列主元
    :param a: 系数矩阵数组
    :param b: 常数项数组
    :param k: 要交换的主元下标
    :return: True：交换成功，False: 奇异
    """
    n = len(b)
    max = abs(a[k][k])
    l = k
    for i in range(k + 1, n):
        if abs(a[i][k]) > max:
            max = abs(a[i][k])
            l = i
    # 奇异
    if max == 0:
        return False
    # 非奇异
    elif l != k:
        for i in range(k, n):
            a[k][i], a[l][i] = a[l][i], a[k][i]
        b[k], b[l] = b[l], b[k]
    return True


def gaussian_eliminate(a, b):
    """
    Solves the linear equation set ``a * x = b`` for the unknown ``x``
    for square ``a`` matrix.
    :param a: 表示x的系数矩阵的二维数组
    :param b: 方程组的常数项一位数组
    :return: 线性方程组的解一维数组ans
    """

    n = len(b)
    # 从主元a[i][i]开始,依次消除后面行的第i列元素
    # 实际并未将其变为0,仅是跳过不再处理(k = i+1),减少不必要的已知操作
    for i in range(0, n):  # i控制主元所在的行
        # 交换主元
        if switch_principal(a, b, i) is False:
            print("该方程组为奇异，无解")
            return None

        for j in range(i + 1, n):  # j控制待置零的行
            factor = a[j][i] / a[i][i]

            for k in range(i + 1, n):  # k控制待置零行的列
                a[j][k] -= factor * a[i][k]  # 更新对应主元后面的a[j][i]元素
            b[j] -= factor * b[i]

    ans = np.zeros(n)
    ans[n - 1] = b[n - 1] / a[n - 1][n - 1]
    # 至底向上回代求解
    for i in range(n - 2, -1, -1):
        sum = b[i]
        for j in range(i + 1, n):
            sum -= ans[j] * a[i][j]
        ans[i] = sum / a[i][i]

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

    print("求解答案：\n", gaussian_eliminate(a, b))
