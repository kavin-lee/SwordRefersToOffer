#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 下午10:04
# @Author  : Kavin-lee
# @Email   : kavin_lee@yeah.net
# @File    : No4.py
# @Software: PyCharm

'''
No.4 重建二叉树
题目描述
输入某二叉树的前序遍历和中序遍历的结果
请重建出该二叉树
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#思路:
#根据前序遍历和中序遍历确定出中点
#然后使用递归进行建树
def reconstruction_binary_tree(pre,tin):
    #判断是不是前序和和后序遍历
    if not pre or not tin:
        return None
    #根节点肯定是前序遍历的第一个元素
    root=TreeNode(pre[0])
    #根据根节点找到中序遍历中的根节点所在的位置,即为中心节点
    mid=tin.index(pre[0])
    #使用递归思想建立根节点的左子树
    root.left=reconstruction_binary_tree(pre[1:mid+1],tin[:mid])
    root.right=reconstruction_binary_tree(pre[mid+1:],tin[mid+1:])
    return root

if __name__ == '__main__':
    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    aa=reconstruction_binary_tree(pre,tin)
    print(aa)
