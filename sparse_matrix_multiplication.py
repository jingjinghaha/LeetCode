'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return None
        hashA = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    continue
                if i not in hashA:
                    hashA[i] = {}
                    hashA[i][j] = A[i][j]
                else:
                    hashA[i][j] = A[i][j]
        hashB = {}
        for j in range(len(B[0])):
            for i in range(len(B)):
                if B[i][j] ==0:
                    continue
                if j not in hashB:
                    hashB[j] = {}
                    hashB[j][i] = B[i][j]
                else:
                    hashB[j][i] = B[i][j]
        results = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for row in hashA:
            for col in hashB:
                for idx in hashA[row]:
                    if idx in hashB[col]:
                        results[row][col] += hashA[row][idx] * hashB[col][idx]
        return results
