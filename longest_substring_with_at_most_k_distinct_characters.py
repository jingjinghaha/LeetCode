'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0
        left = 0
        right = -1
        max_len = 0
        diff_table = {}
        while left < len(s) and right < len(s):
            if len(diff_table) <= k:
                right += 1
                if right < len(s):
                    if s[right] not in diff_table:
                        diff_table[s[right]] = 1
                    else:
                        diff_table[s[right]] += 1
                if right - left > max_len:
                    max_len = right - left
            else:
                diff_table[s[left]] -= 1
                if diff_table[s[left]] == 0:
                    del diff_table[s[left]]
                left += 1
        return max_len
