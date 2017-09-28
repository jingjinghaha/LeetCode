'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# iteratively: BFS
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        from collections import deque
        q1 = deque()
        q2 = deque()
        q1.append(root.left)
        q2.append(root.right)
        while q1 and q2:
            size1 = len(q1)
            size2 = len(q2)
            if size1 != size2:
                return False
            for i in range(size1):
                left = q1.popleft()
                right = q2.popleft()
                if left.val != right.val:
                    return False
                if not left.right and right.left:
                    return False
                if left.right and not right.left:
                    return False
                if left.right and right.left:
                    q1.append(left.right)
                    q2.append(right.left)
                if not left.left and right.right:
                    return False
                if left.left and not right.right:
                    return False
                if left.left and right.right:
                    q1.append(left.left)
                    q2.append(right.right)
        return True

# recursively: DFS
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            is_left_right = self.helper(left.left, right.right)
            is_right_left = self.helper(left.right, right.left)
            if is_left_right and is_right_left:
                return True
        return False
