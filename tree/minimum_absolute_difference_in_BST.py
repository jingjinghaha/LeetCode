'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff, max, min = self.helper(root)
        return min_diff
    
    def helper(self, root):
        if not root:
            return sys.maxint, -sys.maxint, sys.maxint
        if not root.left and not root.right:
            return sys.maxint, root.val, root.val
        
        left_min_diff, left_max, left_min = self.helper(root.left)
        right_min_diff, right_max, right_min = self.helper(root.right)
        
        min_diff = min(abs(left_max-root.val), abs(right_min-root.val), left_min_diff, right_min_diff)
        return min_diff, max(root.val, right_max), min(root.val, left_min)
