'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        stack = []
        indicator = False
        while root:
            if root == p:
                indicator = True
                break
            if root.val < p.val:
                root = root.right
            else:
                stack.append(root)
                root = root.left
        if indicator == False:
            return None
        if root.right:
            root = root.right
            while root.left:
                root = root.left
            return root
        if stack:
            return stack[-1]
        return None

# more tricky
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        succ = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                succ = root
                root = root.left
        return succ
