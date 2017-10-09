'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
# time: O(m+n); space: O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        merge = [0] * length
        i = 0
        j = 0
        idx = 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                merge[idx] = nums2[j]
                j += 1
                idx += 1
                continue
            if j >= len(nums2):
                merge[idx] = nums1[i]
                i += 1
                idx += 1
                continue
            if nums1[i] < nums2[j]:
                merge[idx] = nums1[i]
                i += 1
            else:
                merge[idx] = nums2[j]
                j += 1
            idx += 1
        if length % 2 != 0:
            return merge[length/2]
        else:
            return (merge[(length-1)/2] + merge[length/2])/2.0

# time: O(m+n); space: O(1)
ass Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import sys
        total = len(nums1) + len(nums2)
        i = 0
        j = 0
        count = 0
        prev = -sys.maxint
        cur = -sys.maxint
        while count < total / 2 + 1:
            count += 1
            if i >= len(nums1):
                prev = cur
                cur = nums2[j]
                j += 1
                continue
            if j >= len(nums2):
                prev = cur
                cur = nums1[i]
                i += 1
                continue
            if nums1[i] > nums2[j]:
                prev = cur
                cur = nums2[j]
                j += 1
            else:
                prev = cur
                cur = nums1[i]
                i += 1
        if total % 2 != 0:
            return cur
        return (prev + cur) / 2.0

# time: O(lgm + lgn); space: O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            return (self.findKth(nums1, 0, nums2, 0, total / 2) + self.findKth(nums1, 0, nums2, 0, total / 2 + 1)) / 2.0
        else:
            return self.findKth(nums1, 0, nums2, 0, total / 2 + 1)
        
    def findKth(self, A, i, B, j, k):
        print i,j,k
        if len(A) - i > len(B) - j:
            return self.findKth(B, j, A, i, k)
        if len(A) - i == 0:
            return B[k + j - 1]
        
        if k == 1:
            return min(A[i], B[j])
        
        k1 = min(k / 2, len(A) - i)
        k2 = k - k1
        print k1,k2,k
        if A[i+k1-1] == B[j+k2-1]:
            return A[k1-1]
        elif A[i+k1-1] > B[j+k2-1]:
            return self.findKth(A, i, B, j+k2, k-k2)
        else:
            return self.findKth(A, i+k1, B, j, k-k1)

