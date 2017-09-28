'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''
# time: O(n)
# space: O(n)
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        times = {}
        for val in s:
            if val not in times:
                times[val] = 1
            else:
                times[val] = (times[val] + 1) % 2
        if sum(times.values()) > 1:
            return False
        else:
            return True
