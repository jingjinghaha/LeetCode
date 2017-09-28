'''
Implement pow(x, n).
'''
# the brute force will TLE
# O(lgn) solution, recursive solution
# T(n) = T(n/2) + O(1) = O(lgn)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        if n % 2 == 0:
            return self.myPow(x**2, n/2)
        else:
            return x * self.myPow(x**2, n/2)
