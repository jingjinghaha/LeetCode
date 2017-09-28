'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        return self.helper(0, 0, len(inorder)-1, preorder, inorder)
    def helper(self, pre_start, in_start, in_end, preorder, inorder):
        if pre_start >= len(preorder) or in_start > in_end:
            return None
        root = TreeNode(preorder[pre_start])
        tmp = inorder[in_start:in_end+1].index(preorder[pre_start])
        tmp += in_start
        root.left = self.helper(pre_start + 1, in_start, tmp - 1, preorder, inorder)
        root.right = self.helper(pre_start + tmp - in_start + 1, tmp + 1, in_end, preorder, inorder)
        return root

