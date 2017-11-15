'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum = 0
        for num in nums:
            sum += num
        if k <= 0 or k > len(nums) or sum % k != 0:
            return False
        nums.sort(reverse = True)
        visited = [0] * len(nums)
        target = sum / k
        def helper(k, start, cur_sum, cnt):
            if k == 1:
                return True
            if cur_sum == target and cnt > 0:
                return helper(k-1, 0, 0, 0)
            for i in range(start, len(nums)):
                if visited[i] == 0 and cur_sum + nums[i] <= target:
                    visited[i] = 1
                    if helper(k, i+1, cur_sum + nums[i], cnt + 1):
                        return True
                    visited[i] = 0
            return False
        return helper(k, 0, 0, 0)
        

