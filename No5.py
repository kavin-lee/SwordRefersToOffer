#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 下午10:31
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No5.py
# @Software: PyCharm

'''
No.5 用两个栈实现队列
题目描述
用两个栈来实现一个队列
完成队列的Push和Pop操作
队列中的元素为int类型
'''
class Solution:
    def __init__(self):
        self.list1=[]
        self.list2=[]

    #入栈
    def push(self,val):
        self.list1.append(val)

    #出栈
    def pop(self):
        if self.list2:
            return self.list2.pop()
        else:
            while self.list1:
                self.list2.append(self.list1.pop())
            return self.list2.pop()