'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = 1
            else:
                mapping[s[i]] += 1
        max_odd = 0
        cnt = 0
        indicator = False
        for key in mapping:
            if mapping[key] %2 == 0:
                cnt += mapping[key]
            else:
                indicator = True
                cnt += mapping[key] - 1
        if indicator == True:
            cnt += 1
        return cnt
