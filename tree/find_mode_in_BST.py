'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# simple solution by merging mappings from left child and right child
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mapping, max_cnt = self.helper(root)
        print mapping, max_cnt
        results = []
        for key in mapping:
            if mapping[key] == max_cnt:
                results.append(key)
        return results
    
    def helper(self, root):
        mapping = {}
        cnt = 0
        if not root:
            return {}, 0
        
        left_mapping, left_cnt = self.helper(root.left)
        right_mapping, right_cnt = self.helper(root.right)
        
        mapping = left_mapping
        for key in right_mapping:
            if key not in mapping:
                mapping[key] = right_mapping[key]
            else:
                mapping[key] += right_mapping[key]
            cnt = max(mapping[key], left_cnt, right_cnt)
        if root.val not in mapping:
            mapping[root.val] = 1
        else:
            mapping[root.val] += 1
        cnt = max(mapping[root.val], left_cnt, right_cnt)
        
        return mapping, cnt


