'''
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(len(postorder)-1, 0, len(inorder)-1, inorder, postorder)
    def helper(self, post_end, in_start, in_end, inorder, postorder):
        if post_end < 0 or in_start > in_end:
            return None
        root = TreeNode(postorder[post_end])
        tmp = inorder[in_start:in_end+1].index(root.val)
        tmp += in_start
        root.left = self.helper(post_end-(in_end-tmp+1), in_start, tmp-1, inorder, postorder)
        root.right = self.helper(post_end-1, tmp+1, in_end, inorder, postorder)
        return root

