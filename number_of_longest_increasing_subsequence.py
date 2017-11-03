'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect,sys
        if not nums:
            return 0
        dp = [1] * len(nums)
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == 1:
                cnt[i] = 1
            else:
                for j in range(i):
                    if dp[j] == dp[i] - 1 and nums[j] < nums[i]:
                        cnt[i] += cnt[j]
        longest = max(dp)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == longest:
                ans += cnt[i]
        return ans

# more tricky
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect,sys
        if not nums:
            return 0
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
        longest = max(dp)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == longest:
                ans += cnt[i]
        return ans

