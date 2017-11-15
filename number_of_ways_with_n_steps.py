# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:21:02 2017

@author: jingjing
"""
from collections import deque

def bfs(matrix, n):
    if n <= 0:
        return 1
    q = deque()
    q.append((0,0))
    res = 0
    while len(q):
        size = len(q)
        tmp = 0
        for i in range(size):
            X, Y = q.popleft()
            deltaX = [1, 1, 2, 2, -1, -1, -2, -2]
            deltaY = [2, -2, -1, 1, 2, -2, -1, 1]
            for j in range(8):
                x = X + deltaX[j]
                y = Y + deltaY[j]
                if check(x, y, len(matrix), len(matrix[0])):
                    tmp += 1
                    q.append((x, y))
        res += (tmp - res)
        n -= 1
        if n == 0:
            break
    return res

def check(x, y,m ,n):
    return x >= 0 and x < m and y >= 0 and y < n
    
def dfs(matrix, n):
    if n <= 0:
        return 1
    return helper(matrix, n, 0, 0)

def helper(matrix, n, i, j):
    if n == 0:
        return 1
    res = 0
    deltaX = [1, 1, 2, 2, -1, -1, -2, -2]
    deltaY = [2, -2, -1, 1, 2, -2, -1, 1]
    for k in range(8):
        x = i + deltaX[k]
        y = j + deltaY[k]
        if check(x, y, len(matrix), len(matrix[0])):
            res += helper(matrix, n-1, x, y)
    return res

def dp(matrix, n):
    if n <= 0:
        return 1
    map = {}
    for i in range(12):
        map[i] = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            deltaX = [1, 1, 2, 2, -1, -1, -2, -2]
            deltaY = [2, -2, -1, 1, 2, -2, -1, 1]
            for k in range(8):
                x = i + deltaX[k]
                y = j + deltaY[k]
                if check(x, y, len(matrix), len(matrix[0])):
                    map[matrix[x][y]].append(matrix[i][j])
#    print map
    dp = [[0 for i in range(12)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(12):
            for value in map[j]:
                dp[i][j] += dp[i-1][value]
#    print dp
    return sum(dp[-1])
    
matrix = [[0,1,2],[3,4,5],[6,7,8],[10,9,11]]
n = 15
print bfs(matrix, n)
print dfs(matrix, n)
print dp(matrix, n)