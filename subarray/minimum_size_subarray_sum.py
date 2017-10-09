'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''
# O(n^2)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        presum = [0]
        ans = sys.maxint
        for i in range(len(nums)):
            presum.append(presum[-1]+nums[i])
        for j in range(1, len(presum)):
            for i in range(j):
                if presum[j] - presum[i] >= s:
                    ans = min(ans, j - i)
        if ans == sys.maxint:
            return 0
        return ans

# two pointers, O(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if not nums:
            return 0
        left = 0
        right = 0
        sum = nums[0]
        ans = sys.maxint
        while left < len(nums):
            while right < len(nums)-1 and sum < s:
                right += 1
                sum += nums[right]
            if sum < s:
                break
            if sum >= s:
                ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1
        if ans == sys.maxint:
            return 0
        return ans

# binary search, O(nlgn)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import sys
        import bisect
        if not nums:
            return 0
        presum = [0]
        ans = sys.maxint
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])
        for j in range(1, len(presum)):
            target = presum[j] - s
            i = bisect.bisect(presum, target)
            if i > 0:
                ans = min(ans, j - i + 1)
        if ans == sys.maxint:
            return 0
        return ans
