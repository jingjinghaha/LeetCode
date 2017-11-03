'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        stack = [root]
        cur = root
        while cur.left:
            stack.append(cur.left)
            cur = cur.left
        if cur != root and not cur.right:
            sum += cur.val
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                cur = node.right
                while cur.left:
                    stack.append(cur.left)
                    cur = cur.left
                if cur != node.right and not cur.right:
                    sum += cur.val
        return sum

# easy solution as we don't care the order of the leaves
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = 0
        stack = [root]
        while len(stack):
            cur = stack.pop()
            if cur.left != None:
                if cur.left.left == None and cur.left.right == None:
                    sum += cur.left.val
                else:
                    stack.append(cur.left)
            if cur.right != None:
                if cur.right.left != None or cur.right.right != None:
                    stack.append(cur.right)
        return sum
