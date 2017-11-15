# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:24:56 2017

@author: jingjing
"""

#给出一个tree, 每一个node都有一个value, 问tree里面相同value的node连接成最长路径的大小(edge的数量).
#tree是要自己建的, 输入是两个array, 第一个array表示每个node的value, 第二个array表示所有的边
#例如[1,1,1], [1,2,1,3] -> 2, 说明这个tree有3个node, value都是1, 然后node1和node2有边, node1和node3也有边

res = 0
def longest_univalue_path(A,B):
    
    graph = []
    for i in range(len(A)):
        graph.append([])
    for j in range(0, len(B), 2):
        graph[B[j] - 1].append(B[j+1] - 1)
        graph[B[j+1] - 1].append(B[j] - 1)
    visited = [False] * len(A)
    
    def helper(node):
        global res
        paths = [0]
        for next in graph[node]:
            if not visited[next] and A[next] == A[node]:
                visited[next] = True
                tmp = helper(next) + 1
                paths.append(tmp)
        paths.sort()
        if len(paths) > 1:
            if paths[-1] != 0 and paths[-2] != 0:
                res = max(res, paths[-1] + paths[-2])
            elif paths[-1] != 0:
                res = max(res, paths[-1])
        return paths[-1]
    
    for i in range(len(A)):
        if not visited[i]:
            visited[i] = True
            helper(i)
    print res
    return res


longest_univalue_path([1,1,1,2,2],  [1,2,1,3,2,4,2,5])