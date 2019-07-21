#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 下午4:00
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No12.py
# @Software: PyCharm

'''
No.12 数值的整数次方
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
'''

'''
思路1:直接进行幂运算
'''

def Power(base, exponent):
    return base ** exponent

'''
思路2:不用幂运算,自己累成
'''

def Power1(base, exponent):
    result = 1.0
    if not base:
        return 0.0
    exp = abs(exponent)
    for i in range(exp):
        result *= base
    if exponent > 0:
        return result
    else:
        return 1 / result

if __name__ == '__main__':
    print(Power(5.0,2))
    print(Power1(5.0,2))