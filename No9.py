#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 下午1:15
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No9.py
# @Software: PyCharm

'''
No.9 变态跳台阶
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

'''
解题1

如果是n级台阶，假设有F(n)种跳法，那一定也是先跳1级或者先跳2级……或者n-1级，或者直接跳到n级。
跳1级后有F(n-1)种，跳2级后有F(n-2)种……跳n-1级有F(1)种，直接跳到n级台阶为1种，
故有F(n)=F(n-1)+F(n-2)+……+F(1)+1
'''


def jumpFloorII(n):
    if n < 0:
        return 0
    elif n < 3:
        return n
    else:
        a = [1, 2]
        for i in range(2, n):
            a.append(sum(a) + 1)
        return a[n - 1]


'''
思路2

每一级台阶跳或不跳都有两种
一级台阶有1种，2^0种
二级台阶，第一级台阶跳或者不跳，2^1种
三级台阶，第一级台阶跳或者不跳，2种，第二级台阶跳或者不跳，2种，共2^2种
n级台阶……共2^{n-1}种，即F(n) = 2^(n-1)
'''


def jumpFloorII1(n):
    if n <= 0:
        return 0
    else:
        return 2 ** (n - 1)


if __name__ == '__main__':
    print(jumpFloorII(0))
    print(jumpFloorII1(0))
