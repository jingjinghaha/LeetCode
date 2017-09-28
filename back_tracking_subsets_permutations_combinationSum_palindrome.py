'''
permutations
'''
'''
Given a collection of distinct numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        results = []
        self.helper(nums, [], results)
        return results
    
    def helper(self, nums, tmp, results):
        if len(tmp) == len(nums):
            results.append(tmp)
            return
        for i in xrange(len(nums)):
            if nums[i] not in tmp:
                self.helper(nums, tmp+[nums[i]], results)

'''
permutation II, consider duplicates
'''
class Solution(object):
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        nums.sort()
        results = []
        used = [0] * len(nums)
        self.helper(nums, [], used, results)
        return results
    
    def helper(self, nums, tmp, used, results):
        if len(tmp) == len(nums):
            results.append(tmp)
            return
        for i in xrange(len(nums)):
            if used[i]:
                continue
            if i and nums[i] == nums[i-1] and not used[i-1]:
                continue
            used[i] = 1
            self.helper(nums, tmp+[nums[i]], used, results)
            used[i] = 0


'''
subsets
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.helper(nums, 0, [], results)
        return results
    
    def helper(self, nums, start, tmp, results):
        results.append(tmp)
        if len(tmp) == len(nums):
            return
        for i in xrange(start, len(nums)):
            self.helper(nums, i + 1, tmp+[nums[i]], results)

'''
subsets II
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.helper(nums, 0, [], results)
        return results
    
    def helper(self, nums, start, tmp, results):
        results.append(tmp)
        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.helper(nums, i + 1, tmp+[nums[i]], results)

'''
combination sum
'''
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
        self.helper(candidates, 0, [], target, results)
        return results
    
    def helper(self, candidates, start, tmp, target, results):
        if target == 0:
            results.append(tmp)
            return
        for i in xrange(start, len(candidates)):
            if target >= candidates[i]:
                self.helper(candidates, i, tmp + [candidates[i]], target - candidates[i], results)

'''
combination sum II
'''
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
        self.helper(candidates, 0, [], target, results)
        return results
    
    def helper(self, candidates, start, tmp, target, results):
        if target == 0:
            results.append(tmp)
            return
        for i in xrange(start, len(candidates)):
            if target < candidates[i]:
                break
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.helper(candidates, i+1, tmp+[candidates[i]], target-candidates[i], results)

'''
palindrome partitioning 
'''
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution(object):
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        results = []
        self.helper(s, 0, [], results)
        return results
    
    def helper(self, s, start, tmp, results):
        if start == len(s):
            results.append(tmp)
            return
        for i in xrange(start, len(s)):
            if self.is_palindrome(s[start:i+1]):
                self.helper(s, i+1, tmp+[s[start:i+1]], results)
                
    def is_palindrome(self, s):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True



