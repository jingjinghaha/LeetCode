'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        left_has = self.hasPathSum(root.left, sum - root.val)
        right_has = self.hasPathSum(root.right, sum - root.val)
        if left_has or right_has:
            return True
        return False

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        results = []
        self.helper(root, sum, [], results)
        return results
    def helper(self, root, sum, tmp, results):
        if not root:
            return []
        if root.val == sum and root.left is None and root.right is None:
            results.append(tmp + [root.val])
        self.helper(root.left, sum - root.val, tmp + [root.val], results)
        self.helper(root.right, sum - root.val, tmp + [root.val], results)

'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# the hard part is that the path does not need to start or end at the root or a leaf
# this remind me of presum preprocessing which commonly used in subarray problems
class Solution(object):
    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.helper(root, sum, [0])
        return self.count
    def helper(self, root, sum, presum):
        if not root:
            return
        newsum = presum[-1] + root.val
        for i in range(len(presum)):
            if newsum - presum[i] == sum:
                self.count += 1
        self.helper(root.left, sum, presum+[newsum])
        self.helper(root.right, sum, presum+[newsum])

# notice that going over the presum array is time consuming, can we do it in O(1) time?
# store the presum information into a map
class Solution(object):
    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        mapping = {}
        mapping[0] = 1
        self.helper(root, sum, 0, mapping)
        return self.count
    def helper(self, root, sum, cur_sum, mapping):
        if not root:
            return
        cur_sum += root.val
        if cur_sum - sum in mapping:
            self.count += mapping[cur_sum - sum]
        if cur_sum not in mapping:
            mapping[cur_sum] = 1
        else:
            mapping[cur_sum] += 1
        
        self.helper(root.left, sum, cur_sum, mapping)
        self.helper(root.right, sum, cur_sum, mapping)
        mapping[cur_sum] -= 1

# however, we use globla variable, it is kind of dangerous. So it is better to use loccal variables.
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        mapping = {}
        mapping[0] = 1
        return self.helper(root, sum, 0, mapping)
    def helper(self, root, sum, cur_sum, mapping):
        if not root:
            return 0
        count = 0
        cur_sum += root.val
        if cur_sum - sum in mapping:
            count += mapping[cur_sum - sum]
        if cur_sum not in mapping:
            mapping[cur_sum] = 1
        else:
            mapping[cur_sum] += 1
        count += self.helper(root.left, sum, cur_sum, mapping) + self.helper(root.right, sum, cur_sum, mapping)
        mapping[cur_sum] -= 1
        return count

'''
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:
Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:
Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
'''

