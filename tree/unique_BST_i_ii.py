'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# DFS, TLE
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        tmp = 0
        for i in range(n):
            tmp += self.numTrees(i) * self.numTrees(n - i - 1)
        return tmp

# memorized DFS
class Solution(object):
    mapping = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        tmp = 0
        for i in range(n):
            if i in self.mapping:
                left = self.mapping[i]
            else:
                left = self.numTrees(i)
                self.mapping[i] = left
            if n - i - 1 in self.mapping:
                right = self.mapping[n - i - 1]
            else:
                right = self.numTrees(n - i - 1)
                self.mapping[n - i - 1] = right
            tmp += left * right
        return tmp

# iteratively
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        F = [0] * (n + 1)
        F[0] = 1
        F[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                F[i] += F[j - 1] * F[i - j]
        return F[n]



'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# DFS, accepted
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.helper(1, n)
    def helper(self, start, end):
        trees = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            left = self.helper(start, i - 1)
            right = self.helper(i + 1, end)
            for tree1 in left:
                for tree2 in right:
                    node = TreeNode(i)
                    node.left = tree1
                    node.right = tree2
                    trees.append(node)
        return trees


