'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
'''
# brute force, presum, O(n^2)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        presum = [0]
        ans = -sys.maxint
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        for j in range(1, len(presum)):
            for i in range(j):
                if presum[j] - presum[i] == k:
                    ans = max(ans, j - i)
        if ans == -sys.maxint:
            return 0
        return ans

# presum + hash table, O(n)?
# presum_idx stores a vector of idx, but this is not neccessary. 
# store the for first appearence of one presum is enough.
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        if not nums:
            return 0
        presum_idx = {}
        presum_idx[0] = [0]
        presum = [0]
        tmp_sum = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            presum.append(tmp_sum)
            if tmp_sum not in presum_idx:
                presum_idx[tmp_sum] = [i+1]
            else:
                presum_idx[tmp_sum].append(i+1)
        ans = -sys.maxint
        for j in range(1, len(presum)) :
            if presum[j] - k in presum_idx:
                for idx in presum_idx[presum[j]-k]:
                    if j > idx:
                        ans = max(ans, j - idx)
        if ans == -sys.maxint:
            return 0
        return ans

 # better implementation of previous one, real O(n)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import sys
        if not nums:
            return 0
        presum_idx = {}
        presum_idx[0] = 0
        presum = [0]
        tmp_sum = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            presum.append(tmp_sum)
        ans = -sys.maxint
        for j in range(1, len(presum)) :
            if presum[j] - k in presum_idx:
                ans = max(ans, j - presum_idx[presum[j]-k])
            if presum[j] not in presum_idx:
                presum_idx[presum[j]] = j
        if ans == -sys.maxint:
            return 0
        return ans

