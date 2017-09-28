'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        left = 0
        right = len(nums) - 1
        return self.helper(nums, left, right)
        
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root
