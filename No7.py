#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 下午12:31
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No7.py
# @Software: PyCharm

'''
No.7 斐波那契数列
题目描述
现在要求输入一个整数n
输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

理解
斐波那契数列
因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……
在数学上，斐波纳契数列以如下被以递推的方法定义：
F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
'''


# 方法1:按照Python独有的交换方法进行
def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


# 方法2:构建列表进行计算,保存输出
def Fibonacci1(n):
    a = [0, 1]
    if n <= 1:
        return a[n]
    else:
        for i in range(2, n + 1):
            #添加到列表
            a.append(a[i - 1] + a[i - 2])
        return a[n]


if __name__ == '__main__':
    print(Fibonacci(0))
    print(Fibonacci1(0))
