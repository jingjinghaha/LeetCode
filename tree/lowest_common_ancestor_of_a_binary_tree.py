'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        has_p, has_q, ans =  self.helper(root, p, q)
        if has_p and has_q:
            return ans
        else:
            return None
    def helper(self, root, p, q):
        if not root:
            return False, False, root

        left_has_p, left_has_q, left = self.helper(root.left, p, q)
        right_has_p, right_has_q, right = self.helper(root.right, p, q)
        
        if left_has_p and left_has_q:
            return True, True, left
        if right_has_p and right_has_q:
            return True, True, right

        return (left_has_p or right_has_p or root == p), (left_has_q or right_has_q or root == q), root

