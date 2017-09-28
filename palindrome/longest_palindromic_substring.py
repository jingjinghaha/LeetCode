'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if len(s) < 2:
            return s
        ans = s[0]
        for i in range(len(s)):
            if len(s) - i <= len(ans) / 2:
                break
            left = i
            right = i
            while right < len(s) - 1 and s[right+1] == s[right]:
                right += 1
            i = right + 1
            while left > 0 and right < len(s) - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            if len(s[left:right+1]) > len(ans):
                ans = s[left:right+1]
        return ans
