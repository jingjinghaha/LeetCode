'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
# DP, O(n)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        largest = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            dp = nums[i] + max(dp, 0)
            if dp > largest:
                largest = dp
        return largest

# divide & conquer, O(nlgn)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        m = n / 2
        left_max = self.maxSubArray(nums[0:m])
        right_max = self.maxSubArray(nums[m:n])
        left_sum = -sys.maxint
        right_sum = -sys.maxint
        tmp_sum = 0
        for i in range(m, n):
            tmp_sum += nums[i]
            right_sum = max(right_sum, tmp_sum)
        tmp_sum = 0
        for i in range(m-1, -1, -1):
            tmp_sum += nums[i]
            left_sum = max(left_sum, tmp_sum)
        ans = max(left_max, right_max, left_sum + right_sum)
        return ans

