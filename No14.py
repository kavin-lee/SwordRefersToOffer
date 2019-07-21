#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 下午5:14
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No14.py
# @Software: PyCharm

'''
No.14 链表中倒数第k个结点
题目描述
输入一个链表，输出该链表中倒数第k个结点。
理解
链表详解
python数据结构之链表
'''

'''
设置2个指针，第一个指针走k步之后，第二个指针开始从头走，
这样两个指针之间始终相隔k，当指针1走到链表结尾时，指针2的位置即倒数k个节点 。
'''

def FindKthToTail(head,k):
    if not head or k<=0:
        return None
    p1=head
    p2=head
    #先让指针1:p1走k步
    for _ in range(k-1):
        if not p1.next:
            return None
        p1=p1.next
    while p1.next != None:
        p1=p1.next
        p2=p2.next
    return p2

