'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   
Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None
        start = 0
        end = 0
        while end < len(s):
            if s[end] == '(':
                break
            end += 1
        root = TreeNode(int(s[start: end]))
        if end == len(s):
            return root
        start = end + 1
        end += 1
        stack = ['(']
        while end < len(s):
            if s[end] == '(':
                stack.append('(')
            if s[end] == ')':
                stack.pop()
                if stack == []:
                    break
            end += 1
        left = s[start: end]
        root.left = self.str2tree(left)
        if end == len(s):
            return root
        start = end + 2
        right = s[start: -1]
        root.right = self.str2tree(right)
        return root

