'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.
'''
# O(m*n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        dp[0][1] = 1
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
#O(m)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cur = [1] * n
        for i in xrange(1, m):
            for j in xrange(n):
                if j:
                    cur[j] += cur[j-1]
        return cur[n-1]

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
# O(m*n)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in xrange(n+1)] for j in xrange(m+1)]
        dp[0][1] = 1
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
# O(m)
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cur = [0] * n
        for j in xrange(n):
            if obstacleGrid[0][j] != 1:
                cur[j] = 1
            else:
                break
        for i in xrange(1, m):
            for j in xrange(0, n):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif j:
                    cur[j] += cur[j-1]
        return cur[n-1]

