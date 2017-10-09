'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if not nums:
            return None
        largest = nums[0]
        local_max = nums[0]
        local_min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                tmp = local_max
                local_max = local_min
                local_min = tmp
            local_max = max(nums[i], nums[i]*local_max)
            local_min = min(nums[i], nums[i] *local_min)
            largest = max(largest, local_max)
        return largest
