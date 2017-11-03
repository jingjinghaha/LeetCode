'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        islands = set()
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = []
                    startX = i
                    startY = j
                    q.append((i, j))
                    visited.add((i, j))
                    island.append((i-startX, j-startY))
                    while len(q):
                        size = len(q)
                        for pos in range(size):
                            node = q.popleft()
                            deltaX = [-1, 1, 0, 0]
                            deltaY = [0, 0, -1, 1]
                            for idx in range(4):
                                newX = node[0] + deltaX[idx]
                                newY = node[1] + deltaY[idx]
                                if self.check(newX, newY, m, n) and grid[newX][newY] == 1 and (newX, newY) not in visited:
                                    q.append((newX, newY))
                                    visited.add((newX, newY))
                                    island.append((newX - startX, newY - startY))
                    print island
                    s = str(island)
                    if s not in islands:
                        islands.add(s)
        return len(islands)
    
    def check(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n

