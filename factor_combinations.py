'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 3:
            return []
        result = []
        self.helper(n, -1, [], result)
        return result
    def helper(self, n, lower, tmp, result):
        import math
        if lower != -1:
            result.append(tmp + [n])
        upper = int(math.sqrt(n))
        for i in range(max(2, lower), upper+1):
            if n % i == 0:
                self.helper(n/i, i, tmp + [i], result)

