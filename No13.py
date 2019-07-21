#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 下午4:10
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : N013.py
# @Software: PyCharm

'''
No.13 调整数组顺序使奇数位于偶数前面
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


# 创建奇数偶数列表分别存放最后拼接
def reOrderArray(target):
    list1 = []
    list2 = []
    for item in target:
        if item % 2 == 0:
            list2.append(item)
        else:
            list1.append(item)
    return list1 + list2


# 思路和第一种一样,只是将判断奇数偶数转换为位运算进行判断
def reOrderArray1(target):
    odd = [i for i in target if i & 1]
    eve = [j for j in target if not j & 1]
    return odd + eve



# 前后同时进行移动,如果前面是偶数,后面是奇数,则交换位置
# 元素的顺序会改变


if __name__ == '__main__':
    target = [1, 2, 3, 4, 5, 6, 11, 13, 15, 8]
    print(reOrderArray(target))
    print(reOrderArray1(target))
