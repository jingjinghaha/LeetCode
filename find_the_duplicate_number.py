'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

# must not modify the array means sorting is not allowed
# only use constant space means cannot use binary search after storing and sorting the elements have been passed
# time should be less than O(n^2) meads cannot use brute force solution
# as we already know the range of the value is [1,n], get the mid value and count how many number in the input is less or equal to the mid, if count is larger than mid, shift right to mid, otherwise shift left to mid+1
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        left = 1
        right = n
        while left < right:
            mid = (left + right) / 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


