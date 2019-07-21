#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 下午10:34
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No2.py
# @Software: PyCharm

'''
No.2 替换空格
题目描述
请实现一个函数：
将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''


# 方法1:利用字符串的replace方法直接进行替换
def change_replace(target, param):
    return target.replace(' ', param)


# 方法2:利用循环遍历依次查找替换
def change_replace1(target, param):
    new_target = ''
    for i in target:
        if i == ' ':
            i = param
        new_target += i
    return new_target
#序列化为列表在进行比较判断
def change_replace2(target,param):
    new_target=list(target)
    for i in range(len(new_target)):
        if new_target[i]==' ':
            new_target[i]=param
    return ''.join(new_target)


if __name__ == '__main__':
    target = 'We Are Happy'
    print(change_replace(target, '%20'))
    print(change_replace1(target, '%20'))
    print(change_replace2(target, '%20'))
