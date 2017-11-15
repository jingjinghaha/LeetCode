# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:19:23 2017

@author: jingjing
"""

from collections import deque
import sys
def main():
#    line = raw_input()
#    n, m = line.strip().split(' ')
#    n = int(n)
#    m = int(m)
#    matrix = [[' ' for _ in range(m)] for _ in range(n)]
#    start = None
#    end = None
#    for i in range(n):
#        line = raw_input()
#        for j in range(m):
#            matrix[i][j] = line[j]
#            if matrix[i][j] == 'A':
#                start = (i, j)
#            if matrix[i][j] == 'B':
#                end = (i, j)
    m = 4
    n = 4
    matrix = [['A','#','*','*'],['#','#','#','*'],['*','#','#','#'],['*','*','#','B']]
    start = (0, 1)
    end = (3,3)    
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    deltaX = [0,0,-1,1,1,1,-1,-1]
    deltaY = [-1,1,0,0,1,-1,1,-1]
    def check(x,y):
        return x >= 0 and x < n and y >= 0 and y < m
    indicator = False
    while len(q):
        print q
        node = q.popleft()
        x = node[0]
        y = node[1]
        for k in range(8):
            new_x = x + deltaX[k]
            new_y = y + deltaY[k]
            if check(new_x, new_y) and matrix[new_x][new_y] in '#B' and (new_x, new_y) not in visited:
                if k == 0 or k == 1:
                    if check(new_x + 1, new_y) and matrix[new_x + 1][new_y] == '#':
                        if check(new_x - 1, new_y) and matrix[new_x - 1][new_y] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if k == 2 or k == 3:
                    if check(new_x, new_y + 1) and matrix[new_x][new_y + 1] == '#':
                        if check(new_x, new_y - 1) and matrix[new_x][new_y - 1] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if k == 4:
                    if check(new_x -1, new_y) and matrix[new_x - 1][new_y] == '#':
                        if check(new_x, new_y - 1) and matrix[new_x][new_y - 1] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if k == 5:
                    if check(new_x -1, new_y) and matrix[new_x - 1][new_y] == '#':
                        if check(new_x, new_y + 1) and matrix[new_x][new_y + 1] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if k == 6:
                    if check(new_x +1, new_y) and matrix[new_x + 1][new_y] == '#':
                        if check(new_x, new_y - 1) and matrix[new_x][new_y - 1] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))
                if k == 7:
                    if check(new_x +1, new_y) and matrix[new_x + 1][new_y] == '#':
                        if check(new_x, new_y + 1) and matrix[new_x][new_y + 1] == '#':
                            if (new_x, new_y) == end:
                            	indicator = True
                            	print True
                                break
                            q.append((new_x, new_y))
                            visited.add((new_x, new_y))

    if indicator == False:
        print False
    
if __name__ == '__main__':
	main()