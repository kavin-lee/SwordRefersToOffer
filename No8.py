#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 下午12:50
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No8.py
# @Software: PyCharm

'''
No.8 跳台阶
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''


# 思路:
# 1层台阶-->1种
# 2层台阶-->2种
# 3层台阶-->3种
# 4层台阶-->5种   由此可以看出是斐波那契数列的问题

def jumpFloor(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a + b
        return b


def jumpFloor1(n):
    a = [1, 2]
    if n <= 2:
        return a[n - 1]
    else:
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2])
        return a[n - 1]


if __name__ == '__main__':
    print(jumpFloor(4))
    print(jumpFloor1(4))
