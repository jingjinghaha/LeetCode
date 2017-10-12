'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        presum_hash = {}
        sum = 0
        presum_hash[0] = 1
        result = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in presum_hash:
                result += presum_hash[sum-k]
            if sum not in presum_hash:
                presum_hash[sum] = 1
            else:
                presum_hash[sum] += 1
        return result
