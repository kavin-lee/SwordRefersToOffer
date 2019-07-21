#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 下午2:29
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No11.py
# @Software: PyCharm
import time

'''
No.11 二进制中1的个数
题目描述
输入一个整数，输出该数二进制表示中1的个数。
其中负数用补码表示。
'''

'''
思路:
先将判断该数是否为正数,整数不用转化,若果是负整数,则需要进行转换(正数)
要使用n & 0xFFFFFFFF得到一个数的补码
'''


def NumberOf1(num):
    if num < 0:
        num = num & 0xFFFFFFFF
    return bin(num).count('1')


if __name__ == '__main__':
    start = time.time()
    print(NumberOf1(50))
    end=time.time()
    print("时间:%.2f"%(end-start))
