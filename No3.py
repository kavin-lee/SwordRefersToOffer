#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 下午10:54
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No3.py
# @Software: PyCharm

'''
No.3 从尾到头打印链表
题目描述
输入一个链表：
按链表值从尾到头的顺序返回一个ArrayList。
链表结构
'''


# 创建单链表的节点
class NodeList:
    def __init__(self, value):
        self.value = value
        self.next = None



def reverse_output(target):
    ArrayList=[]
    while target:
        ArrayList.append(target.value)
        target=target.next
    return ArrayList[::-1]


if __name__ == '__main__':
    aa=reverse_output(NodeList)
    print(aa)