#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author    : Nam Zeng
# @Time      : 2018/12/31 14:34
# @Desc      : 使用贝尔斯托夫法（Bairstov method)求解多项式方程的全部近似解


def get_du_dv(coe_a, coe_b, coe_c):
    """
    求二元一次方程组的解，相应行列式：a0 b0 | c0
                                   a1 b1 | c1
    :param coe_a:系数[a0, a1]
    :param coe_b:系数[b0, b1]
    :param coe_c:常数[c0, c1]
    :return: 变量du, dv
    """
    D0 = coe_a[0] * coe_b[1] - coe_a[1] * coe_b[0]
    Du = coe_c[0] * coe_b[1] - coe_c[1] * coe_b[0]
    Dv = coe_a[0] * coe_c[1] - coe_a[1] * coe_c[0]
    if D0 == 0:
        return None
    else:
        du = Du / D0
        dv = Dv / D0
        return [du, dv]


def get_root(u, v):
    """
    求解一元二次方程x^2 + ux +v的解
    :param u, v: 系数
    :return: 近似解list[]
    """
    delta = u ** 2 - 4 * v
    if delta >= 0:
        # 误差处理
        if u >= 0:
            x1 = (u + delta ** 0.5) / (-2)
            x2 = (-2 * v) / (u + delta ** 0.5)
        else:
            x1 = (-1 * u + delta ** 0.5) / 2
            x2 = 2 * v / (-1 * u + delta ** 0.5)
        if x1 == x2:
            return [x1]
        else:
            return [x1, x2]
    else:
        # 解为复数
        x1 = complex(u / (-2), (-1 * delta) ** 0.5 / 2)
        x2 = complex(u / (-2), (-1 * delta) ** 0.5 / (-2))
        # -1表示解为复数
        return [x1, x2, -1]


def get_r_s_b(a, u0, v0):
    """
    求r0,r1,s0, s1, 以及商多项式的系数bn
    :param a:多项式系数列表[a0,a1,...,an]
    :param u0, v0: 初始二次方程x^2 + ux +v的近似系数
    :return: list[r0,r1,s0,s1,b[]]
    """
    n = len(a) - 1
    b = [0 for i in range(n + 1)]

    # 求b[n]
    b[0] = a[0]
    b[1] = a[1] - u0 * b[0]
    for k in range(2, n + 1):
        b[k] = a[k] - u0 * b[k - 1] - v0 * b[k - 2]
    # 求r0 , r1
    r0 = b[n - 1]
    r1 = b[n] + u0 * b[n - 1]

    c = [0 for i in range(n - 1)]
    c[0] = b[0]
    c[1] = b[1] - u0 * b[0]
    for k in range(2, n - 1):
        c[k] = b[k] - u0 * c[k - 1] - v0 * c[k - 2]
    # 求s0 , s1
    s0 = c[n - 3]
    s1 = c[n - 2] + u0 * c[n - 3]
    del c

    lt = [r0, r1, s0, s1]
    lt.append(b)
    return lt


def bairstov(a, N, tol):
    """
    求多项式方程的全部近似解
    :param a:多项式系数列表[a0,a1,...,an]
    :param N:最大迭代次数
    :param tol: 容差
    :return: 近似解的列表ans[root_1[], root_2[]]
    """
    roots_1 = []  # 存实数根
    roots_2 = []  # 存复数根
    ans = []

    # 初始化循环变量
    n = len(a) - 1
    if a[n - 2] == 0:
        u0 = -1
        v0 = -1
    else:
        u0 = a[n - 1] / a[n - 2]
        v0 = a[n] / a[n - 2]
    for k in range(N):
        if len(a) == 3:        # 当为二次式时，直接求根
            lt_3 = get_root(u0, v0)
            if len(lt_3) < 3:  # 为实数根
                roots_1.extend(lt_3)
            else:              # 为复数根
                del lt_3[2]
                roots_2.append(lt_3)
            break;
        if len(a) == 2:        # 当为一次时，直接求实数根
            rt = -1 * a[1] / a[0]
            roots_1.append(rt)
            break
        else:
            # 求r0,r1,s0,s1,bn
            lt_1 = get_r_s_b(a, u0, v0)
            b = lt_1[4]
            # 求行列式系数
            coe_a = [u0 * lt_1[2] - lt_1[3], v0 * lt_1[2]]
            coe_b = [-1 * lt_1[2], -1 * lt_1[3]]
            coe_c = [-1 * lt_1[0], -1 * lt_1[1]]
            # 求du, dv
            lt_2 = get_du_dv(coe_a, coe_b, coe_c)
            u0 = u0 + lt_2[0]
            v0 = v0 + lt_2[1]
            # 满足误差条件时，直接求根
            if abs(lt_2[0]) < tol and abs(lt_1[1]) < tol:
                lt_3 = get_root(u0, v0)
                if len(lt_3) < 3:
                    roots_1.extend(lt_3)
                else:
                    del lt_3[2]
                    roots_2.append(lt_3)
                a = b[0:-2]
    if k == N:
        ans = None
    else:
        ans.append(roots_1)
        ans.append(roots_2)
    return ans


if __name__ == '__main__':
    # 测试用例： X^5 - 3.5X^4 + 2.75X^3 + 2.125X^2 - 3.875X + 1.25 = 0
    # 设置最大迭代次数N=1000, 容差tol=0.0001
    coe_list = [1, -3.5, 2.75, 2.125, -3.875, 1.25]
    # coe_list = [1, 0, 0, 8]
    ans = bairstov(coe_list, 1000, 0.0001)
    if ans is None:
        print("求解失败!\n")
    else:
        ans_1 = ans[0]
        ans_2 = ans[1]
        print("多项式方程的实数根为：")
        for k in range(len(ans_1)):
            print(ans_1[k])
        print("\n多项式方程的复数根为：")
        for k in range(len(ans_2)):
            x = print(ans_2[k])
