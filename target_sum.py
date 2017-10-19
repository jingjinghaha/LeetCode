'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''
# DFS, TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count = 0
        self.helper(nums, S, 0)
        return self.count
    def helper(self, nums, target, start):
        if start == len(nums):
            if target == 0:
                self.count += 1
            return
        self.helper(nums, target - nums[start], start + 1)
        self.helper(nums, target + nums[start], start + 1)

# memorized DFS, accepted
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.helper(nums, S, 0, 0, {})
    def helper(self, nums, target, idx, tmp, mapping):
        key = str(idx) + "->" + str(tmp)
        if key in mapping:
            return mapping[key]
        if idx == len(nums):
            if tmp == target:
                return 1
            return 0
        cnt1 = self.helper(nums, target, idx + 1, tmp - nums[idx], mapping)
        cnt2 = self.helper(nums, target, idx + 1, tmp + nums[idx], mapping)
        mapping[key] = cnt1 + cnt2
        return mapping[key]


