# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:00:46 2017

@author: jingjing
"""

# A = [(1,2), (3,4), (7,10), (15,16)]
# B = [(0,2), (3,8), (8,12), (16,17)]
# output: [(1,2), (3,4), (7,8), (8,10), (16,16)]

def overlap(A, B):
    i = 0
    j = 0
    res = []
    while i < len(A) and j < len(B):
        print i, j
        while j < len(B) and A[i][0] > B[j][1]:
            # j += 1
            j = bisearch(A[i][0], B)
        while i < len(A) and A[i][1] < B[j][0]:
            # i += 1
            i = bisearch(B[j][0], A)
        if i < len(A) and j < len(B):
            res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            elif A[i][1] > B[j][1]:
                j += 1
            else:
                if i < len(A) - 1 and j < len(B) - 1 and A[i+1][0] == A[i][1] and B[j+1][0] == B[j][1]:
                    res.append([A[i][1], B[j+1][0]])
                    res.append([B[j][1], A[i+1][0]])
                    i += 1
                    j += 1
                elif i < len(A) - 1 and A[i+1][0] == A[i][1]:
                    i += 1
                elif j < len(A) - 1 and B[j+1][0] == B[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
    return res

def bisearch(val, array):
    import bisect, numpy
    array = numpy.array(array)
    pos = bisect.bisect_left(array[:,1], val)
    return pos
    
#A = [(1,2), (3,4), (7,10), (12,16)]
#B = [(0,2), (3,8), (8,10), (10,17)]
A = [(1,2), (1000,1001)]
B = [(1,2), (2,2), (3,4), (5,6), (1000,1001)]
print overlap(A, B)
