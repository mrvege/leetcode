# !/usr/bin/env python
# encoding: utf-8
__author__ = 'dm'
"""
differnt from 235, the problem based on a tree which not ranked
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
        __3______
       /         \
    ___5__    ___1__
   /      \  /      \
   6      2  0       8
         /  \
         7   4

思路分析：
用的深搜的方法
从根节点开始分别遍历左右子树，深搜从root到p和到q的路径
在找到路径上第一个公共节点
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==None or root==p or root==q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if  l and r:
            return root
        elif l:
            return l
        elif r:
            return r
        else:
            return None


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    s1 = Solution()
    print s1.lowestCommonAncestor(root, root.left.right, root.left.right.left).val