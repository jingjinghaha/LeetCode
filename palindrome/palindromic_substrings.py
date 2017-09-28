'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        count = len(s)
        i = 0
        while i < len(s):
            print i
            left = i
            right = i
            while right < len(s) - 1 and s[right+1] == s[right]:
                right += 1
            i = right + 1
            print i
            cnt = right - left + 1
            count += cnt * (cnt - 1) / 2
            prev = left
            while left > 0 and right < len(s) - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            if left < prev:
                count += prev - left
        return count
