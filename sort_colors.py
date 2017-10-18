'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
'''
# count # of each value first
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        counts = [0] * 3
        for i in range(len(nums)):
            counts[nums[i]] += 1
        idx = 0
        for i in range(3):
            while counts[i]:
                nums[idx] = i
                idx += 1
                counts[i] -= 1

# two-pointers
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = 0
        r = len(nums) - 1
        i = 0
        
        while i <= r:
            # print l,r,i
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                tmp = nums[l]
                nums[l] = nums[i]
                nums[i] = tmp
                l += 1
                i += 1
            else:
                tmp = nums[r]
                nums[r] = nums[i]
                nums[i] = tmp
                r -= 1

# more tricky, pay attention that swap 2 before swap 0
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = 0
        r = len(nums) - 1
        i = 0
        while i <= r:
            while nums[i] == 2 and i < r:
                tmp = nums[r]
                nums[r] = nums[i]
                nums[i] = tmp
                r -= 1
            while nums[i] == 0 and i > l:
                tmp = nums[l]
                nums[l] = nums[i]
                nums[i] = tmp
                l += 1
            i += 1
