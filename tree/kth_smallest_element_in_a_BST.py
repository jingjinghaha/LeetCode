'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = 0
        stack = []
        result = []
        stack.append(root)
        while root.left:
            stack.append(root.left)
            root = root.left
        while stack:
            node = stack.pop()
            result.append(node.val)
            count += 1
            if count == k:
                return result[-1]
            if node.right:
                stack.append(node.right)
                node = node.right
                while node.left:
                    stack.append(node.left)
                    node = node.left

