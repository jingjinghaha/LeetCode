'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        results = []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if left != []:
            for path in left:
                s = str(root.val) + '->' + path
                results.append(s)
        if right != []:
            for path in right:
                s = str(root.val) + '->' + path
                results.append(s)
        return results
