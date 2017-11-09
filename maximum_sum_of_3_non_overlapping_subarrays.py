'''
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 3 * k:
            return []
        n = len(nums)
        m = len(nums) - k + 1
        sums = [0] * m
        max_left = [0] * m
        max_right = [0] * m
        # presum of k continuous elements
        local_sum = 0
        for i in range(n):
            local_sum += nums[i]
            if i >= k -1:
                sums[i - k + 1] = local_sum
                local_sum -= nums[i - k + 1]
        # the maximal k continuous elements sum from left to right and the correspoding idx
        maxv, maxi = 0, 0
        for i in range(m):
            if sums[i] > maxv:
                maxv, maxi = sums[i], i
            max_left[i] = (maxv, maxi)
        # the maximal k continuous elements sum from right to left and the correspoding idx
        maxv, maxi = 0, 0
        for i in range(m-1, -1, -1):
            if sums[i] > maxv:
                maxv, maxi = sums[i], i
            max_right[i] = (maxv, maxi)
        ansv, ansi = 0, []
        for i in range(k, m - k):
            v1, i1 = max_left[i - k]
            v2, i2 = max_right[i + k]
            if sums[i] + v1 + v2 > ansv:
                ansv = sums[i] + v1 + v2
                ansi = [i1, i, i2]
        return ansi

