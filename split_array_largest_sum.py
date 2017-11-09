'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
# binary search, the smallest subarray sum is max(nums), the largest subarray sum is sum(nums)
# get the middle value, to see if the array can be split into m subarrays or less than m subarrays. If it can, shift the right value to the middle, if it can split the array more than m times, shift the left value to the middle
# keep doing this until left is not less than right, then return left
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = left + (right - left) / 2
            if self.can_split(nums, m, mid):
                right = mid
            else:
                left = mid + 1
        return left
    def can_split(self, nums, m, sum):
        cnt = 1
        local_sum = 0
        for i in range(len(nums)):
            local_sum += nums[i]
            if local_sum > sum:
                cnt += 1
                local_sum = nums[i]
                if cnt > m:
                    return False
        return True 
