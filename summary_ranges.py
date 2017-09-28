'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        i = 0
        ans = []
        while i < len(nums):
            start = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] - nums[i] == 1:
                i += 1
                j += 1
            if nums[i] == start:
                ans.append(str(start))
            else:
                ans.append(str(start)+"->"+str(nums[i]))
            i += 1
        return ans
