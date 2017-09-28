'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
# convert to string 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None:
            return False
        if x < 0:
            return False
        s = str(x)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# use math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x is None:
            return False
        if x < 0:
            return False
        if x != 0 and x % 10 == 0:
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x/10
        if x == reverse or x == reverse / 10:
            return True
        else:
            return False
