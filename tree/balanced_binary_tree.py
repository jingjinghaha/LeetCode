'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, height = self.helper(root)
        return is_balanced
    def helper(self, root):
        if not root:
            return True, 0
        is_left, left_h = self.helper(root.left)
        is_right, right_h = self.helper(root.right)
        height = max(left_h, right_h) + 1
        if is_left and is_right and abs(left_h - right_h) <= 1:
            return True, height
        return False, height

