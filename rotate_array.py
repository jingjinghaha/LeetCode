'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        l = len(nums)
        k = k % l
        if k > 0:
            self.reverse(nums, 0, l-k-1)
            self.reverse(nums, l-k, l-1)
            nums.reverse()
    
    def reverse(self, nums, left, right):
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1



class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return
        n = len(nums)
        if k == n or k == 0:
            return
        k %= n
        print k
        tmp_array = []
        for i in range(n - k, n):
            tmp_array.append(nums[i])
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k - 1, -1, -1):
            nums[i] = tmp_array[i]

