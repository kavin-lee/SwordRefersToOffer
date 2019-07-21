#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 下午4:32
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No10.py
# @Software: PyCharm

'''
No.10 矩形覆盖
题目描述
我们可以用21的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个21的小矩形无重叠地覆盖一个2n的大矩形，总共有多少种方法？
'''

'''
理解
n个21的小矩形 覆盖 2*n的大矩形
覆盖方式：横着或者竖着
本质上还是斐波那契数列问题
矩形覆盖问题分析
F(0) = 0
F(1) = 1
F(2) = 2
F(n) = F(n-1) + F(n-2) (n>2)
'''


def rectCover(n):
    if n < 0:
        return 0
    elif n < 3:
        return n
    else:
        a = [1, 2]
        for i in range(2, n):
            a.append(a[i - 1] + a[i - 2])
        return a[n - 1]



if __name__ == '__main__':
    print(rectCover(4))