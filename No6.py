#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 上午11:39
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No6.py
# @Software: PyCharm

'''
No.6 旋转数组的最小数字
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
给出的所有元素都大于0，若数组大小为0，请返回0。
'''
#思路:简而言之,就是找到数组中得最小值
#方法1
def find_min(target):
    if len(target)==0:
        return 0
    else:
        return min(target)

#方法2
def find_min1(target):
    if len(target)>0:
        target_min=target[0]
        for item in target:
            if target_min>item:
                target_min=item
        return target_min
    else:
        return 0

if __name__ == '__main__':
    target=[1,2,3,4,5]
    print(find_min(target))
    print(find_min1(target))
