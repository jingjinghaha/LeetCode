'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            # target in the left half and nums[mid] in the right half
            elif nums[mid] < nums[0] and target >= nums[0]:
                right = mid
            # target is the right half and nums[mid] in the left half
            elif nums[mid] >= nums[0] and target < nums[0]:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        # to make sure there is no duplicate nums[0] in the right half
        while right > 1 and nums[right] == nums[right - 1]:
            right -= 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return True
            # target in the left half and nums[mid] in the right half
            elif nums[mid] < nums[0] and target >= nums[0]:
                right = mid
            # target is the right half and nums[mid] in the left half
            elif nums[mid] >= nums[0] and target < nums[0]:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        return False

