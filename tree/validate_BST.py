'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import sys
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_valid, max, min = self.helper(root)
        return is_valid
    def helper(self, root):
        if not root:
            return True, -sys.maxint, sys.maxint
        
        is_left, left_max, left_min = self.helper(root.left)
        is_right, right_max, right_min = self.helper(root.right)
        
        if is_left and is_right:
            if left_max < root.val < right_min:
                root_max = max(right_max, root.val)
                root_min = min(left_min, root.val)
                return True, root_max, root_min
        return False, 0, 0 

