'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''
# O(m*n)
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums or not nums:
            return []
        mapping = {}
        for i in range(len(nums)):
            mapping[nums[i]] = i
        results = []
        for num in findNums:
            indicator = False
            if num in mapping:
                idx = mapping[num]
                while idx < len(nums):
                    if nums[idx] > num:
                        results.append(nums[idx])
                        indicator = True
                        break
                    idx += 1
            if indicator == False:
                results.append(-1)
        return results

# O(m+n)
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums or not nums:
            return []
        mapping = {}
        for i in range(len(findNums)):
            mapping[findNums[i]] = i
        stack = []
        results = [-1]*len(findNums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if nums[i] in mapping:
                if stack:
                    results[mapping[nums[i]]] = stack[-1]
            stack.append(nums[i])
        return results



'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''
# consider the input as twice larger if it is a circular array
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        stack = []
        results = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            stack.append(nums[i])
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                results[i] = stack[-1]
            stack.append(nums[i])
        return results

'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
'''
# traverse from right, find the first element that its right neighbor is larger than it. 
# find the smallest element is the right of it and swap them
# sort the elements in the right as increasing order
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or len(str(n)) < 2:
            return -1
        s = list(str(n))
        indicator = False
        for i in range(len(s)-1, 0, -1):
            if s[i] > s[i-1]:
                indicator = True
                break
        print i
        if indicator == True:
            j = self.find_next_large(s[i:], s[i-1])
            tmp = s[i-1]
            s[i-1] = s[i+j]
            s[i+j] = tmp
            self.quick_sort(s, i, len(s)-1)
            result = int(''.join(s))
            if result > 2**31 - 1:
                return -1
            return result
        else:
            return -1
        
    def find_next_large(self, s, val):
        left = 0
        right = len(s) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if s[mid] > val:
                left = mid
            else:
                right = mid
        if s[right] > val:
            return right
        else:
            return left
    
    def quick_sort(self, s, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = s[(start+end)/2]
        while left <= right:
            while left <= right and s[left] < pivot:
                left += 1
            while left<=right and s[right] > pivot:
                right -= 1
            if left <= right:
                tmp = s[left]
                s[left] = s[right]
                s[right] = tmp
                left += 1
                right -= 1
        self.quick_sort(s, start, right)
        self.quick_sort(s, left, end)


