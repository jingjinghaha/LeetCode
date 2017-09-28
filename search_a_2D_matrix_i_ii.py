'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''
# lgm + lgn
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        if matrix[left][0] == target or matrix[right][0] == target:
            return True
        if matrix[right][0] < target:
            row = right
        else:
            row = left
        
        left = 0
        right = n -1
        while left + 1 < right:
            mid = (left + right) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid
            else:
                left = mid
        if matrix[row][left] == target or matrix[row][right] == target:
            return True
        else:
            return False

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
# O(mlgn)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        for row in xrange(m):
            if matrix[row][0] > target:
                break
            if matrix[row][0] <= target and matrix[row][n-1] >= target:
                import bisect
                pos = bisect.bisect_left(matrix[row], target)
                if matrix[row][pos] == target:
                    return True
        return False

# O(m+n)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1
        while i <= m-1 and j >= 0:
            print i, j
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
