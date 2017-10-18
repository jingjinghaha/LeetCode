'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s

