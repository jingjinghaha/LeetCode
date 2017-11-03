'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d:
                return [d[tmp], i]
            else:
                d[nums[i]] = i


'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
# two pointers
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                return [i + 1, j + 1]
            elif s < target:
                i += 1
            else:
                j -= 1
# binary search
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        for i in range(len(nums)-1):
            if i and nums[i] == nums[i - 1]:
                continue
            tmp = target - nums[i]
            pos = bisect.bisect_left(nums[i+1:], tmp)
            if pos < len(nums) - i - 1 and nums[pos+i+1] == tmp:
                return [i+1, i+pos+2]
        return [-1, -1]

'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
'''
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.hashmap:
            self.hashmap[number] = 1
        else:
            self.hashmap[number] += 1            

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.hashmap:
            tmp = value - num
            if tmp == num and self.hashmap[tmp] < 2:
                continue
            if tmp in self.hashmap:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        from collections import deque
        q = deque()
        q.append(root)
        hashset = set()
        hashset.add(root.val)
        while len(q):
            node = q.popleft()
            if node.left:
                tmp = k - node.left.val
                if tmp in hashset:
                    return True
                q.append(node.left)
                hashset.add(node.left.val)
            if node.right:
                tmp = k - node.right.val
                if tmp in hashset:
                    return True
                q.append(node.right)
                hashset.add(node.right.val)
        return False

