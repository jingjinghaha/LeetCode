'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        mapping = {}
        mapping[0] = -1
        sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sum += 1
            else:
                sum -= 1
            if sum in mapping:
                ans = max(ans, i - mapping[sum])
            if sum not in mapping:
                mapping[sum] = i
        return ans
