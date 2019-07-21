#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 下午8:31
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No1.py
# @Software: PyCharm
'''
No.1 二维数组的查找
题目描述
在一个二维数组中（每个一维数组的长度相同）
每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


# 方法1:循环遍历数组,拿到每一个元素与目标元素作比较
# 相等则返回True 不等则返回False,(此时间复杂度n²)
def find_int(target, num):
    for i in range(len(target)):
        for j in range(len(target[i])):
            if target[i][j] == num:
                return True
    return False


# 方法2:以最后一行的第一个元素为基准作对比
# 若目标大于此基准,行数不变,往后找
# 若目标小于此基准,列数不变,行数向前找
# 否则视为找到此对象
def find_int1(target, num):
    rows = len(target) - 1  # 总行数
    cols = len(target[0]) - 1  # 每行的元素数
    #从后开始
    i=rows
    #第一个元素
    j=0
    while i>=0 and j<=cols:
        #判断是否小于目标
        if target[i][j]<num:
            j+=1
        #判断是否大于目标
        elif target[i][j]>num:
            i-=1
        else:
            return True
    return False



if __name__ == '__main__':
    target = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8],
        [5, 6, 7, 8, 9],
    ]
    print(find_int(target, 1))
    print(find_int1(target, 1))
