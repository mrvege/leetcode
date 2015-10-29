__author__ = 'Administrator'
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"""

#Definition for a binary tree node.
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
        if root==None or p==None or q ==None:
            return None
        if max(p.val, q.val)<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val)>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    s1 = Solution()
    print s1.lowestCommonAncestor(root, TreeNode(7), TreeNode(9)).val
