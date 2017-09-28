'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
# go over the element of the matrix, if the element is 1 and not passed yet, push it into a queue, then find all the elements that can be reached from this element by bfs and mark them as passed
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        passed = set()
        queue = deque()
        count = 0
        deltaX = [0, 0, -1, 1]
        deltaY = [-1, 1, 0, 0]
        
        def check(x, y):
            return x >= 0 and y >= 0 and x < m and y < n
        
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == str(1) and (i, j) not in passed:
                    queue.append([i, j])
                    passed.add((i,j))
                    while queue:
                        size = len(queue)
                        for s in xrange(size):
                            node = queue.popleft()
                            for delta in range(4):
                                newX = node[0]+deltaX[delta]
                                newY = node[1]+deltaY[delta]
                                if check(newX, newY) and grid[newX][newY] == str(1) and (newX, newY) not in passed:
                                    queue.append([newX, newY])
                                    passed.add((newX, newY))
                    count += 1
        return count

