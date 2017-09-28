'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
# when traverse left or up, check whether the row or col still exists to prevent duplicates
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        rowBegin = 0; rowEnd = m - 1
        colBegin = 0; colEnd = n - 1
        
        while rowBegin<=rowEnd and colBegin <= colEnd:
            for i in xrange(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1
            for i in xrange(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBegin<=rowEnd:
                for i in xrange(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -= 1
            if colBegin <= colEnd:
                for i in xrange(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
            colBegin += 1
        return res 

# an easier understanding one from https://soulmachine.gitbooks.io/algorithm-essentials/content/java/simulation/spiral-matrix.html
# keep going while true, break when exceed any boundary in four directions


'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        res = [[0 for i in range(n)] for j in range(n)]
        rowBegin, colBegin = 0, 0 
        rowEnd, colEnd = n - 1, n - 1 
        idx = int(1)
        while idx <= n*n and rowBegin <= rowEnd and colBegin <= colEnd:
            for i in xrange(colBegin, colEnd + 1):
                res[rowBegin][i] = idx
                idx += 1
            rowBegin += 1
            for i in xrange(rowBegin, rowEnd + 1):
                res[i][colEnd] = idx
                idx += 1
            colEnd -= 1
            if rowBegin <= rowEnd:
                for i in xrange(colEnd, colBegin - 1, -1):
                    res[rowEnd][i] = idx
                    idx += 1
            rowEnd -= 1
            if colBegin <= colEnd:
                for i in xrange(rowEnd, rowBegin - 1, -1):
                    res[i][colBegin] = idx
                    idx += 1
            colBegin += 1
        return res 

