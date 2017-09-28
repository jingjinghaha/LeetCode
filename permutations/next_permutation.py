'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

# time: O(n), as the array to be sorted is already reversely sorted, the quick sort only cost O(n)  
# space: O(1), in place
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        flag = False
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                flag = True
                break
        if flag == True:
            idx = self.findnextlarge(nums[i-1], nums[i:])
            tmp = nums[i-1]
            nums[i-1] = nums[i+idx]
            nums[i+idx] = tmp
            self.quicksort(nums, i, len(nums) - 1)
        else:
            self.quicksort(nums, 0, len(nums) - 1)
    
    def findnextlarge(self, target, nums):
        left = 0
        right = len(nums) - 1
        while left+1 < right:
            mid = (left+right)/2
            if nums[mid] > target:
                left = mid
            else:
                right = mid
        if nums[right] > target:
            return right
        if nums[left] > target:
            return left
        return left
    
    def quicksort(self, nums, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = nums[(left+right)/2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1
        self.quicksort(nums, start, right)
        self.quicksort(inums, left, end)

'''
Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. So, elements from num[i] to num[n-1] is reversely sorted.

To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with the smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 121543321, we want to swap the '1' at position 2 with '2' at position 7.

The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the num[i,n-1]
'''
