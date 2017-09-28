'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''
# definitely n^2 solution would not work
# the following presum solution can pass Leetcode, but the best solution is to use binary Indexed Tree or Segment Tree
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.presum = [[0 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    self.presum[i][j] = self.matrix[i][j]
                elif i == 0:
                    self.presum[i][j] = self.presum[i][j-1] + self.matrix[i][j]
                elif j == 0:
                    self.presum[i][j] = self.presum[i-1][j] + self.matrix[i][j]
                else:
                    self.presum[i][j] = self.presum[i-1][j] + self.presum[i][j-1] - self.presum[i-1][j-1] + self.matrix[i][j]
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if not self.matrix:
            return
        orig = self.matrix[row][col]
        self.matrix[row][col] = val
        for i in xrange(row, len(self.matrix)):
            for j in xrange(col, len(self.matrix[0])):
                self.presum[i][j] += (val - orig)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return
        if row1 == 0 and col1 == 0:
            sum = self.presum[row2][col2]
        elif row1 == 0:
            sum = self.presum[row2][col2] - self.presum[row2][col1-1]
        elif col1 == 0:
            sum = self.presum[row2][col2] - self.presum[row1-1][col2]
        else:
            sum = self.presum[row2][col2] - self.presum[row1-1][col2] - self.presum[row2][col1-1] + self.presum[row1-1][col1-1]
        return sum


