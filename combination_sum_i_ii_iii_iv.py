'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        self.helper(candidates, target, 0, [], results)
        return results
    def helper(self, candidates, target, start, tmp, results):
        if target == 0:
            results.append(tmp)
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                break
            self.helper(candidates, target - candidates[i], i, tmp + [candidates[i]], results)

'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []
        self.helper(candidates, target, 0, [], results)
        return results
    def helper(self, candidates, target, start, tmp, results):
        if target == 0:
            results.append(tmp)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if target >= candidates[i]:
                self.helper(candidates, target - candidates[i], i + 1, tmp + [candidates[i]], results)

'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < k or n > 9 * k:
            return []
        results = []
        self.helper(k, n, 0, [], results)
        return results
    def helper(self, k, n, cur, tmp, results):
        if cur == k and n == 0:
            results.append(tmp)
            return
        for i in range(1, 10):
            if n < i:
                break
            if cur and i <= tmp[-1]:
                continue
            self.helper(k, n - i, cur + 1, tmp + [i], results)

'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        hashmap = {}
        return self.helper(nums, target, hashmap)
    def helper(self, nums, target, hashmap):
        if target in hashmap:
            return hashmap[target]
        if target == 0:
            return 1
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                hashmap[target - nums[i]] = self.helper(nums, target - nums[i], hashmap)
                res += hashmap[target - nums[i]]
        return res
# dp 
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
